#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place pywassap tests --exclude=__init__.py
black pywassap tests
isort pywassap tests
