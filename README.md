# draft-modelspec-sbml-api
This repository contains a draft implemention of an SBML API generated using modelspec, addressing this github issue: 
https://github.com/combine-org/compbiolibs/issues/28

It is based on this initial neuroml modelspec api:
https://github.com/ModECI/modelspec/blob/development/examples/neuroml2/neuroml2_spec.py

To replicate my development setup you can follow the steps outlines here:
- https://github.com/UCL-ARC/rjv_vagrant_files/tree/main/comp_bio_libs

Alternatively use any suitable Linux environment with the correct dependencies install (see the ansible [playbook](https://github.com/UCL-ARC/rjv_vagrant_files/blob/main/comp_bio_libs/synced_folder/ansible_local/playbook.yml) for a list of the packages required).

Then follow these steps:

```
#setup environment variables
export BASE_FOLDER=~/repos                      #pick which folder repository gets clone into
export REPO_NAME=draft-modelspec-sbml-api       #must match the repo's actual name
export MODELSPEC_VERSION=0.3.0                  #which version of modelspec to clone and install

#create workspace
mkdir -p ${BASE_FOLDER}
cd ${BASE_FOLDER}
git clone git@github.com:combine-org/${REPO_NAME}.git
cd ${REPO_NAME}
chmod u+x ./sbml3_spec.py

#create and activate the virtual environment
rm -rf ./virtenv
python3 -m venv ./virtenv
. ./virtenv/bin/activate

#download and install modelspec
cd ${BASE_FOLDER}
wget https://github.com/ModECI/modelspec/archive/refs/tags/v${MODELSPEC_VERSION}.tar.gz
tar -xf v${MODELSPEC_VERSION}.tar.gz
cd modelspec-${MODELSPEC_VERSION}
pip install .
cd ${BASE_FOLDER}/${REPO_NAME}

#run the SBML example
./sbml3_spec.py
```