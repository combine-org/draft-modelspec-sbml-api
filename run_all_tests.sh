#!/bin/bash

#
# run all tests
#

source ./includes

if [[ "${VIRT_ENV}" != "${REPO_NAME}/${VIRTENV_NAME}" ]] ; then
    echo Activate the virtual enviroment first using: source ./activate_venv.sh
    exit 1
fi

mkdir -p untracked
mkdir -p test/untracked

pytest #=D
