#!/usr/bin/env bash
set +x -e  # -x:debug mode, -e:cancel on error
if [ -e ".env" ]; then
    set -a; source .env; set +a
fi
set -x -e
python3 -m venv _venv

# flake8
./_venv/bin/pip3 install -qq flake8 pep8-naming coverage
./_venv/bin/flake8 --max-line-length 500 user_analytics/
./_venv/bin/flake8 --max-line-length 500 --ignore=F401 tests

# coverage
./_venv/bin/pip3 install -qqr requirements.txt
./_venv/bin/coverage run --source user_analytics -m unittest discover -s tests
./_venv/bin/coverage report
./_venv/bin/coverage html
