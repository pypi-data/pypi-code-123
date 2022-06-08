import os
import sys
import logging
import tempfile
from pathlib import Path
from getpass import getuser
from functools import lru_cache
from typing import Union, Optional

from . import _mureq as mureq


PYPI_API_URL: str = 'https://pypi.org/pypi/pyright/json'
log: logging.Logger = logging.getLogger(__name__)


def get_env_dir() -> Path:
    """Returns the directory that contains the nodeenv"""
    env_dir = os.environ.get('PYRIGHT_PYTHON_ENV_DIR')
    if env_dir is not None:
        return Path(env_dir)

    try:
        suffix = f'.{getuser()}'
    except Exception:
        suffix = ''

    return Path(tempfile.gettempdir()) / f'pyright-python{suffix}' / 'env'


def env_to_bool(key: str, *, default: bool = False) -> bool:
    value = os.environ.get(key)
    if value is None:
        return default

    return value.lower() in {'1', 't', 'on', 'true'}


def maybe_decode(data: Union[str, bytes]) -> str:
    if isinstance(data, bytes):
        return data.decode(sys.getdefaultencoding())

    return data


@lru_cache(maxsize=None)
def get_latest_version() -> Optional[str]:
    """Returns the latest available version of pyright-python.

    This relies on the JSON PyPi API, if PyPi is down or the user is offline then
    None is returned.
    """
    try:
        response = mureq.get(PYPI_API_URL, timeout=1)
        version = response.json()["info"]["version"]
    except Exception as exc:
        log.debug(
            'Encountered exception while fetching latest release: %s - %s',
            type(exc),
            exc,
        )
        return

    if version.startswith('v'):
        version = version[1:]

    log.debug('Latest pyright-python version is: %s', version)
    return version
