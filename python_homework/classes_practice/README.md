Practice with Python classes.

The `practice.py` and `practice.ipynb` contain same code.


# Environment

Tested on Ubuntu 20.04.3 LTS.

Required Python 3.8-3.10 and venv.

You can install it with:
```console
sudo apt-get install python3.10 python3.10-venv
```

Required git:
```console
sudo apt install git
```

# Install and run with pip
## Installation

```console
git clone https://github.com/Freddsle/BI_2021_Python
cd ./BI_2021_Python/python_homework/classes_practice

# Create and activate your virtual environment

# create virtual environment
python3.10 -m venv ./venv

# activate virtual environment
source ./venv/bin/activate

# if you install it not from main or master, change branch
git checkout classes_task

# required by pip to build wheels
pip install wheel==0.37.0 

# Install requirements
pip install -r ./requirements.txt
```

## Run file
```console
python3.10 practice.py
```

# Install and run with poetry
```console
# install poetry
# for details look for https://python-poetry.org/docs/
sudo apt-get install curl
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3.10 -

# poetry will be accessible in current session
source $HOME/.poetry/env

# prepare project (if you have previously installed poetry - start here)
git clone https://github.com/Freddsle/BI_2021_Python
cd ./BI_2021_Python/python_homework/classes_practice

# if you install it not from main or master, change branch
git checkout classes_task

poetry env use python3.10
poetry install

# Run
poetry run python practice.py
```