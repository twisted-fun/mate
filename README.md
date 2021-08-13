# Mate: Extremely pluggable and modular shell
[![build](https://github.com/twisted-fun/mate/actions/workflows/python-package.yml/badge.svg)](https://github.com/twisted-fun/mate/actions/workflows/python-package.yml)
[![pypi](https://img.shields.io/pypi/v/mate-shell?logo=pypi)](https://pypi.org/project/mate-shell/)
[![](https://img.shields.io/github/license/twisted-fun/mate?logo=github)](https://github.com/twisted-fun/mate/blob/master/LICENSE)
[![codecov](https://codecov.io/gh/twisted-fun/mate/branch/master/graph/badge.svg?token=AIQF2UVD8B)](https://codecov.io/gh/twisted-fun/mate)
[![](https://img.shields.io/github/last-commit/twisted-fun/mate?logo=github)](https://github.com/twisted-fun/mate/commits/master)
[![](https://img.shields.io/badge/sentry-active-brightgreen)](https://sentry.io/organizations/r00t3r/projects/)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=twisted-fun_mate&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=twisted-fun_mate)
## Features
- Easy plugin creation using setuptools
- Manage group of plugins better by `mate --shells`
- Built-in auto complete
- Forced modularity in plugins
- Dope looking shell
- Provides command output redirect to embedded ipython
- Supports batch executions by `mate --exec` and JSON formatted output

## Installation
### Using pypi
```bash
pip3 install mate-shell
```
### Using git
```bash
git clone https://github.com/twisted-fun/mate.git
cd mate
pip3 install -e .
```

## Usage
Hope this [asciinema](https://asciinema.org/a/CcOaU2HRsYV27iCUmMEFygyJQ) will help.

## Plugins
Commands can be added into mate shell as plugins. And it's super easy!
### Writing a plugin
```python
# demo_plugin.py
from mate import add_plugins, command


def sxor(s1, s2):
    return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))


@command(option="xor")
def bitwise_string_xor(self, str1, str2):
    """A bitwise xor operation for two strings."""
    return {"result": sxor(str1, str2).__repr__()}


add_plugins(modules=[bitwise_string_xor])
```
```python
# setup.py
from setuptools import setup

setup(
    name="mate-demo-plugin",
    install_requires="mate-shell",
    entry_points={"mate": ["bitwise_str_xor = demo_plugin"]},
    py_modules=["demo_plugin"],
)
```

### Installing the plugin
```bash
pip3 install -e .
```

### Accessing the plugin
Check out this [asciinema](https://asciinema.org/a/Q46B1et1VTUwwczTJAhgoyk3y).

### More? [Example Plugins](https://github.com/twisted-fun/mate-infosec-plugins)
