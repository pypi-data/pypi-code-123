# QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
# Lean CLI v1.0. Copyright 2021 QuantConnect Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import os
import re
import urllib.request

from setuptools import find_packages, setup

current_dir = os.path.abspath(os.path.dirname(__file__))


def read(relative_path: str) -> str:
    with open(os.path.join(current_dir, relative_path)) as file:
        return file.read()


def get_version() -> str:
    version_file = read("ablean/__init__.py")
    version_match = re.search(r"^__version__ = \"([^\"]+)\"", version_file, re.M)
    return version_match.group(1)


def get_stubs_version_range() -> str:
    if get_version() == "dev":
        return ""

    try:
        response = urllib.request.urlopen("https://pypi.org/pypi/abl-quantconnect-stubs/json").read()
        latest_version = json.loads(response)["info"]["version"]
        return f">={latest_version}"
    except:
        return ""


# Production dependencies
install_requires = [
    "click~=8.1.3",
    "requests~=2.25.1",
    "json5~=0.9.5",
    "rich~=12.4.4",
    "dependency-injector~=4.20.1",
    "pydantic~=1.7.3",
    "python-dateutil~=2.8.1",
    "lxml~=4.6.3",
    "maskpass==0.3.5",
    "joblib~=1.0.1",
    "python-certifi-win32~=1.6",
    "pyshortcuts~=1.8.0",
    "wrapt~=1.12.1",
    "paramiko~=2.11.0",
    "scp~=0.14.4",
    "ptvsd",
    "setuptools",
    f"abl-quantconnect-stubs{get_stubs_version_range()}"
]

setup(
    name="ablean",
    version=get_version(),
    description="A CLI aimed at making it easier to run QuantConnect's LEAN engine locally and in the cloud",
    author="abl",
    author_email="support@quantconnect.com",
    url="https://lean.io/cli",
    long_description=read("README.md").replace("](lean", "](https://github.com/QuantConnect/lean-cli/blob/master/lean"),
    long_description_content_type="text/markdown",
    packages=find_packages(include=["ablean", "ablean.*"]),
    package_data={
        "ablean": ["icons/*"]
    },
    entry_points={
        "console_scripts": ["ablean=ablean.main:main"]
    },
    install_requires=install_requires,
    python_requires=">= 3.8",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ],
    project_urls={
        "Documentation": "https://www.lean.io/docs/lean-cli/key-concepts/getting-started",
        "Source": "https://github.com/QuantConnect/lean-cli"
    },
)
