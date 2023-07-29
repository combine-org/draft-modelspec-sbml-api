#!/usr/bin/env python3

'''
run via pytest (see run_all_test.sh)

tests test4 and test5 are EXPECTED to fail to demonstrate the bug

a minimalist replication of a bug where an unset (optional) id causes an error when trying to write to json

the error will be like to this

Traceback (most recent call last):
  File "/home/vagrant/repos/draft-modelspec-sbml-api/./replicate_id_bug.py", line 62, in <module>
    replicate_id_bug()
  File "/home/vagrant/repos/draft-modelspec-sbml-api/./replicate_id_bug.py", line 58, in replicate_id_bug
    sbml_doc.to_json_file(f"replicate_id_bug.json")
  File "/home/vagrant/repos/draft-modelspec-sbml-api/virtenv/lib/python3.10/site-packages/modelspec/base_types.py", line 168, in to_json_file
    json.dump(self.to_dict(), outfile, indent=4)
  File "/home/vagrant/repos/draft-modelspec-sbml-api/virtenv/lib/python3.10/site-packages/modelspec/base_types.py", line 93, in to_dict
    d = converter.unstructure(self)
  File "/home/vagrant/repos/draft-modelspec-sbml-api/virtenv/lib/python3.10/site-packages/cattrs/converters.py", line 232, in unstructure
    return self._unstructure_func.dispatch(
  File "<cattrs generated unstructure __main__.SBML>", line 7, in unstructure_SBML
    res['model'] = __c_unstr_model(instance.model)
  File "<cattrs generated unstructure __main__.Model>", line 7, in unstructure_Model
    res['listOfUnitDefinitions'] = __c_unstr_listOfUnitDefinitions(instance.listOfUnitDefinitions)
  File "/home/vagrant/repos/draft-modelspec-sbml-api/virtenv/lib/python3.10/site-packages/modelspec/base_types.py", line 915, in f
    d = {o.id: converter.unstructure(o) for o in obj_list}
  File "/home/vagrant/repos/draft-modelspec-sbml-api/virtenv/lib/python3.10/site-packages/modelspec/base_types.py", line 915, in <dictcomp>
    d = {o.id: converter.unstructure(o) for o in obj_list}
  File "/home/vagrant/repos/draft-modelspec-sbml-api/virtenv/lib/python3.10/site-packages/cattrs/converters.py", line 232, in unstructure
    return self._unstructure_func.dispatch(
  File "<cattrs generated unstructure __main__.UnitDefinition>", line 7, in unstructure_UnitDefinition
    res['listOfUnits'] = __c_unstr_listOfUnits(instance.listOfUnits)
  File "/home/vagrant/repos/draft-modelspec-sbml-api/virtenv/lib/python3.10/site-packages/modelspec/base_types.py", line 919, in f
    del objd["id"]
KeyError: 'id'
'''

import json
import yaml

import modelspec
from modelspec import field, instance_of, optional
from modelspec.base_types import Base
from typing import List

def replicate_id_bug(sbml_id=None,model_id=None,unitdef_id=None,unit_id=None,fname=""):
    '''
    minimal replication of the missing 'id' error
    error happens when trying to write to json file
    whereever an item with no id set is part of a list
    even if it's the only item in the list
    items not in lists do not generate the error if their id is unset

    so: unitDef and unit have an id set to avoid the error (although id is supposed to be optional in SBML)
    whereas sbml and model do not need it to be set
    '''

    @modelspec.define
    class SBase(Base):
        id:     str = field(default=None,validator=optional(instance_of(str)))

    @modelspec.define
    class Unit(SBase):
        pass

    @modelspec.define
    class UnitDefinition(SBase):
        listOfUnits: List[Unit] = field(factory=list)

    @modelspec.define
    class Model(SBase):
        listOfUnitDefinitions:     List[UnitDefinition]     = field(factory=list)

    @modelspec.define
    class SBML(SBase):
        model: Model = field(default=None, validator=optional(instance_of(Model)))

    sbml_doc = SBML(id=sbml_id) #no error if no id set

    model = Model(id=model_id) #no error if no id set
    sbml_doc.model = model

    unitDef = UnitDefinition(id=unitdef_id) #error if no id set
    model.listOfUnitDefinitions.append(unitDef)

    unit = Unit(id=unit_id)#error if no id set
    unitDef.listOfUnits.append(unit)

    sbml_doc.to_json_file(f"untracked/test_id_bug.{fname}.json")

def test1():
    'this passes'
    replicate_id_bug(sbml_id="sbml",model_id="model",unitdef_id="unitdef",unit_id="unit",fname="test1")

def test2():
    'this passes'
    replicate_id_bug(sbml_id=None,model_id="model",unitdef_id="unitdef",unit_id="unit",fname="test2")

def test3():
    'this passes'
    replicate_id_bug(sbml_id="sbml",model_id=None,unitdef_id="unitdef",unit_id="unit",fname="test3")

def test4():
    'this fails'
    replicate_id_bug(sbml_id="sbml",model_id="model",unitdef_id=None,unit_id="unit",fname="test4")

def test5():
    'this fails'
    replicate_id_bug(sbml_id="sbml",model_id="model",unitdef_id="unitdef",unit_id=None,fname="test5")
