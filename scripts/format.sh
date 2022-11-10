#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place hiya docs_src tests --exclude=__init__.py
black src tests
isort src tests
