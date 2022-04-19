



# Install and run with poetry
```console
# install poetry
# for details look for https://python-poetry.org/docs/
sudo apt-get install curl
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3.10 -

# poetry will be accessible in current session
source $HOME/.poetry/env

# prepare project
git clone https://github.com/Freddsle/BI_2021_Python
cd ./BI_2021_Python/python_homework/parallel_pracrice/

# if you install it not from main or master, change branch
git checkout parallel_pracrice

poetry env use python3.10
poetry install

# Run
poetry run python parallel_pracrice.py

# or for run .ipynb files
poetry run jupyter notebook

```
