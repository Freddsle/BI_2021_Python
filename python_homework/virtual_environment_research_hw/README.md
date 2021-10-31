This is updated research on virtual environments from https://github.com/krglkvrmn/Virtual_environment_research. 

You can easily reproduce the results by running scripts locally. 

# Environment

Tested on Ubuntu 20.04.3 LTS.

Required Python 3.9 and venv.

You can install it with:
```console
sudo apt-get install python3.9 python3.9-venv
```

Required git:
```console
sudo apt install git
```


# Install and run with pip
## Installation

```console
git clone https://github.com/Freddsle/BI_2021_Python
cd ./BI_2021_Python/python_homework/virtual_environment_research_hw/

# Create and activate your virtual environment

# create virtual environment
python3.9 -m venv ./venv

# activate virtual environment
source ./venv/bin/activate

# Install requirements
pip install -r ./requirements.txt
```

## Run file
```console
python3.9 pain.py
```

# Install and run with poetry
```console
# install poetry
# for details look for https://python-poetry.org/docs/
sudo apt-get install curl
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3.9 -

# poetry will be accessible in current session
source $HOME/.poetry/env

# prepare project
git clone git@github.com:Freddsle/BI_2021_Python.git
cd ./python_homework/virtual_environment_research_hw/

poetry install

# Run
poetry run python pain.py

```

# How to cite
Please cite - the article is available at doi:10.1111/1000-7.
