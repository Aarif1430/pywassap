#!/usr/bin/env bash

set -e
set -x

# mypy src
flake8 src tests docs_src
black src tests docs_src --check
isort src tests docs_src scripts --check-only
