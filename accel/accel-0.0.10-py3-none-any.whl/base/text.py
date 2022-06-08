from pathlib import Path
from typing import List

from accel.base.mols import Mol
from accel.base.tools import change_dir, float_to_str
from accel.util.log import logger


def replace_key(conf: Mol, lines: List[str]):
    _rls = "".join(lines)
    while True:
        if "#NAME#" in _rls:
            _rls = _rls.replace("#NAME#", conf.name)
            continue
        if "#DATA[" in _rls:
            key = _rls.split("#DATA[")[1].split("]#")[0]
            _rls = _rls.replace("#DATA[" + key + "]#", conf.data[key])
            continue
        if "#AXYZ#" in _rls:
            _xyz = [
                "{:<2} {:>15} {:>15} {:>15}".format(
                    _a.symbol,
                    float_to_str(_a.x),
                    float_to_str(_a.y),
                    float_to_str(_a.z),
                )
                for _a in conf.atoms
            ]
            _rls = _rls.replace("#AXYZ#", "\n".join(_xyz))
            continue
        if "#ATOMS#" in _rls:
            _rls = _rls.replace("#ATOMS#", str(len(conf.atoms)))
            continue
        if "#CHG#" in _rls:
            _rls = _rls.replace("#CHG#", str(conf.charge))
            continue
        if "#MULT#" in _rls:
            _rls = _rls.replace("#MULT#", str(conf.multiplicity))
            continue
        if "#ENRGY#" in _rls:
            _rls = _rls.replace("#ENRGY#", str(conf.energy))
            continue
        if "#PATH#" in _rls:
            _rls = _rls.replace("#PATH#", str(conf.path))
            continue
        if "#LABEL#" in _rls:
            _rls = _rls.replace("#LABEL#", str(conf.label))
            continue
        break
    _rls = [_l + "\n" for _l in _rls.split("\n")]
    return _rls[:-1]


def write_input(_c: Mol, template: Path, odir=None, change_path=False):
    _tp = Path(template).resolve()
    if not _tp.exists():
        logger.error(f"{str(_tp)} not exist")
        raise ValueError
    with _tp.open("r") as f:
        _ls = f.readlines()
    _ls = replace_key(_c, _ls)
    _p = change_dir(_c.path, odir, _c.name).with_suffix(_tp.suffix)
    with _p.open("w", newline="\n") as f:
        f.writelines(_ls)
    logger.info(f"{_p.name} created")
    if change_path:
        _c.path = _p
