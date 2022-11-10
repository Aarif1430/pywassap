#!/usr/bin/env bash

set -e
set -x

# mypy src
flake8 src tests
black src tests  --check
isort src tests  scripts --check-only
