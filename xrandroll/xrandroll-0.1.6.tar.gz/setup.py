# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xrandroll']

package_data = \
{'': ['*']}

install_requires = \
['parse>1.0', 'pyedid>=0.1', 'pyside2>5.14']

entry_points = \
{'console_scripts': ['xrandroll = xrandroll:main']}

setup_kwargs = {
    'name': 'xrandroll',
    'version': '0.1.6',
    'description': 'A powertool to configure your display',
    'long_description': '# XRandRoll\n\nNone of the existing display configuration tools does what I think is "the right thing".\nSo I went and wrote one.\n\n## The Right Thing\n\n* Don\'t start from a stored config, use xrandr to read the systems\' current state\n* Allow creating "profiles" that will get applied smartly (not there yet)\n* Generate a xrandr invocation to reflect the desired configuration\n* Allow per-monitor scaling\n* Allow arbitrary monitor positioning\n* Implement "scale everything so all the pixels are the same size"\n\n## To try:\n\nIf you have PySide2: `python -m xrandroll` in the folder where you cloned it (of course deps are a problem,\nthis is experimental code, if you can\'t figure it out it\'s probably better for you 😊).\n\n## TODO:\n\n* Implement other things\n* Forget about it forever\n',
    'author': 'Roberto Alsina',
    'author_email': 'roberto.alsina@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ralsina/xrandroll',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
