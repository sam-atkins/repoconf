# repoconf

<a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

Script to add common repo configuration files.

- [repoconf](#repoconf)
  - [Usage](#usage)
  - [Install](#install)

## Usage

Adds template config files to a repo. Run in the destination i.e. target repo to add these files.

```bash
repoconf --help

usage: repoconf [-h] {python,py,javascript,js,golang,go}

Get language repo setup

positional arguments:
  {python,py,javascript,js,golang,go}

optional arguments:
  -h, --help            show this help message and exit
```

## Install

```bash
# create a virtual environment i.e. venv
python3 -m virtualenv -p python3.7 venv

# activate the venv
source venv/bin/activate

# install dependencies
poetry install
```

After the install command, not only will the dependencies be installed but the script will be enabled to run from the project root directory.

To setup the script to run from any directory, run this in your home directory:

```
python3 -m pip install --user --editable /Users/{username}/path/to/repoconf
```
