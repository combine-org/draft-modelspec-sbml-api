# draft-modelspec-sbml-api
This repository contains a draft implemention of an SBML API generated using modelspec, addressing this issue: 
https://github.com/combine-org/compbiolibs/issues/28

It is based on this initial neuroml modelspec api:
https://github.com/ModECI/modelspec/blob/development/examples/neuroml2/neuroml2_spec.py

This was developed on an ubuntu linux vm under virtualbox. The aim is to document setting up the vm from scratch using Vagrant,
but for now here are the setup steps from the point of having the vm running:

```
## todo: document steps to setup mkvirtualenv

#create workspace folder and virtual environment
export WORKING_DIR=~/cbl_code/modelspec_sbmlapi
mkdir -p ${WORKING_DIR} && cd ${WORKING_DIR}
rm -rf ~/.virtualenvs/modelspec_sbmlapi
mkvirtualenv modelspec_sbmlapi --python=/home/ccaervi/mambaforge/envs/py310/bin/python
deactivate
workon modelspec_sbmlapi

#download and install modelspec
wget https://github.com/ModECI/modelspec/archive/refs/tags/v0.3.0.tar.gz
tar -xf v0.3.0.tar.gz
cd modelspec-0.3.0
pip install .
cd -

#download and run the SBML example
## todo: replace this with a "git clone" and "pip install ."
wget <url>
./sbml3_spec.py
```