# draft-modelspec-sbml-api
This repository contains a draft implemention of an SBML API generated using modelspec, addressing this github issue: 
https://github.com/combine-org/compbiolibs/issues/28

It is based on this initial neuroml modelspec api:
https://github.com/ModECI/modelspec/blob/development/examples/neuroml2/neuroml2_spec.py

This was developed on an ubuntu linux vm under virtualbox. The aim is to document setting up the vm from scratch using Vagrant,
but for now here are the setup steps from the point of having the vm running:

```
## todo: document steps to setup mkvirtualenv

#create workspace folder and virtual environment
export BASE_FOLDER=~/cbl_code                   #pick which folder repository gets clone into
export REPO_NAME=draft-modelspec-sbml-api       #must match the repo's actual name
export VIRTENV_NAME=${REPO_NAME}
export PATH_TO_PYTHON=/home/ccaervi/mambaforge/envs/py310/bin/python #set to the python you want to use
export PATH=${PATH_TO_PYTHON}:${PATH}

mkdir -p ${BASE_FOLDER}
cd ${BASE_FOLDER}
git clone git@github.com:combine-org/${REPO_NAME}.git
cd ${REPO_NAME}
chmod u+x ./sbml_spec.py

rm -rf ~/.virtualenvs/${VIRTENV_NAME}
mkvirtualenv ${VIRTENV_NAME} --python=${PATH_TO_PYTHON}
deactivate
workon ${VIRTENV_NAME}

#download and install modelspec
cd untracked
wget https://github.com/ModECI/modelspec/archive/refs/tags/v0.3.0.tar.gz
tar -xf v0.3.0.tar.gz
cd modelspec-0.3.0
pip install .
cd ${BASE_FOLDER}/${REPO_NAME}

#run the SBML example
./sbml3_spec.py
```