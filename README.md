# repoconf

<a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

- [repoconf](#cookiecutterprojectname)
  - [Usage](#usage)
  - [Install](#install)

## Usage

```bash
repoconf --help
```

## Install

```bash
# create a venv
virtualenv -p python3.7 venv

# activate the venv
source venv/bin/activate

# install dependencies
poetry install
```

After the install command, not only will the dependencies be installed but the script will be enabled to run from the project root directory.

To setup the script to run from any directory, run this in your home directory:

```
pip3 install --editable /Users/{username}/path/to/repoconf
```
