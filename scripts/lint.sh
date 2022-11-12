#!/usr/bin/env bash

set -e
set -x

# mypy src
flake8 pywassap tests
black pywassap tests  --check
isort spywassaprc tests  scripts --check-only
