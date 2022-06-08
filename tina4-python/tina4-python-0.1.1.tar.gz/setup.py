# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tina4_python']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.3,<4.0.0']

entry_points = \
{'console_scripts': ['run = main:main']}

setup_kwargs = {
    'name': 'tina4-python',
    'version': '0.1.1',
    'description': 'Tina4Python - This is not another framework for Python',
    'long_description': None,
    'author': 'Andre van Zuydam',
    'author_email': 'andrevanzuydam@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
