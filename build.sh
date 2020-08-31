#!/bin/sh

PYTHON_VERSION=$(python3 --version | awk '{print $2}')

set -ex
rm -rf ~/.local/lib/python$PYTHON_VERSION/site-packages/mkdocs_pom_parser_plugin-*/
tox
