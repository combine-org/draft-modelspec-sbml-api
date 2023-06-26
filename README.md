# draft-modelspec-sbml-api
This repository contains a draft implemention of an SBML API generated using modelspec, addressing this github issue: 
https://github.com/combine-org/compbiolibs/issues/28

It is based on this initial neuroml modelspec api:
https://github.com/ModECI/modelspec/blob/development/examples/neuroml2/neuroml2_spec.py

This was developed on an ubuntu linux vm under virtualbox configured using Vagrant. The vagrant config is here:
https://github.com/UCL-ARC/rjv_vagrant_files/tree/main/comp_bio_libs. It is a basic linux vm with git and pip installed, and the virtualenv pip module.
Once the basic vm is installed follow the bash commands below:

```
#setup environment variables
export BASE_FOLDER=~/repos                      #pick which folder repository gets clone into
export REPO_NAME=draft-modelspec-sbml-api       #must match the repo's actual name
export VIRTENV_NAME=${REPO_NAME}

#create workspace
mkdir -p ${BASE_FOLDER}
cd ${BASE_FOLDER}
git clone git@github.com:combine-org/${REPO_NAME}.git
cd ${REPO_NAME}
chmod u+x ./sbml_spec.py

#create virtual environment
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