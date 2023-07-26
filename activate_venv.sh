#!/bin/bash

#
# source this file to activate the virtual environment
#

#doesn't work for sourced scripts
#SCRIPT_PATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

#so just assume pwd is the repo's main folder
REPO_PATH=$(pwd)

#set any project related environment variables
source "${REPO_PATH}/includes"

#activate the virtual environment
source "${REPO_PATH}/${VIRTENV_NAME}/bin/activate"
