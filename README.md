# draft-modelspec-sbml-api
This repository contains a draft implemention of an SBML API generated using modelspec, addressing this github issue: 
https://github.com/combine-org/compbiolibs/issues/28

It is based on this initial neuroml modelspec api:
https://github.com/ModECI/modelspec/blob/development/examples/neuroml2/neuroml2_spec.py

To replicate my development setup you can follow the steps outlined here:
- https://github.com/UCL-ARC/rjv_vagrant_files/tree/main/comp_bio_libs

Alternatively you can manually replicate the ansible [playbook](https://github.com/UCL-ARC/rjv_vagrant_files/blob/main/comp_bio_libs/synced_folder/ansible_local/playbook.yml) by installing the require dependencies and cloning the repos into any suitable Linux environment.

Then follow these steps:

```
#note: this repo and modelspec have already been cloned by the ansible playbook
cd repos/draft-modelspec-sbml-api

#oneoff setup to create the virtual environment
./create_venv.sh

#activate the environment
source ./activate_venv.sh

#run the SBML example
./sbml3_spec.py
```