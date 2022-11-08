#!/usr/bin/env bash

set -e
set -x

mypy hiya
flake8 hiya tests docs_src
black hiya tests docs_src --check
isort hiya tests docs_src scripts --check-only
