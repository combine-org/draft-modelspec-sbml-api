#!/bin/bash

#
# delete any existing virtual environment folder
# create a new virtual environment
# install modelspec inside it
# modelspec should already be git cloned 
#

set -eu

#get the path to this script
SCRIPT_PATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

#this currently is the same as the main repo folder
REPO_PATH=${SCRIPT_PATH}

#set any project related environment variables
source "${REPO_PATH}/includes"

cd ${REPO_PATH}
rm -rf ./${VIRTENV_NAME}
python3 -m venv ./${VIRTENV_NAME}
source ./${VIRTENV_NAME}/bin/activate

pip install ${REQUIRED_PIP_PACKAGES}
cd ${MODELSPEC_PATH}
pip install .
