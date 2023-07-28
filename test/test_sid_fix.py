#!/usr/bin/env python3

'''
run via pytest (see run_all_test.sh)

test if changing id to sid prevents the missing 'id' error

(yes it does)
'''

import json
import yaml

import modelspec
from modelspec import field, instance_of, optional
from modelspec.base_types import Base
from typing import List

def replicate_id_bug(sbml_sid=None,model_sid=None,unitdef_sid=None,unit_sid=None,fname=""):
    '''
    no errors when the sbase id is renamed to sid
    '''

    @modelspec.define
    class SBase(Base):
        sid:     str = field(default=None,validator=optional(instance_of(str)))

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

    sbml_doc = SBML(sid=sbml_sid) #no error if no id set

    model = Model(sid=model_sid) #no error if no id set
    sbml_doc.model = model

    unitDef = UnitDefinition(sid=unitdef_sid) #error if no id set
    model.listOfUnitDefinitions.append(unitDef)

    unit = Unit(sid=unit_sid)#error if no id set
    unitDef.listOfUnits.append(unit)

    sbml_doc.to_json_file(f"untracked/test_sid.{fname}.json")

def test1():
    'this passes'
    replicate_id_bug(sbml_sid="sbml",model_sid="model",unitdef_sid="unitdef",unit_sid="unit",fname="test1")

def test2():
    'this passes'
    replicate_id_bug(sbml_sid=None,model_sid="model",unitdef_sid="unitdef",unit_sid="unit",fname="test2")

def test3():
    'this passes'
    replicate_id_bug(sbml_sid="sbml",model_sid=None,unitdef_sid="unitdef",unit_sid="unit",fname="test3")

def test4():
    'this passes'
    replicate_id_bug(sbml_sid="sbml",model_sid="model",unitdef_sid=None,unit_sid="unit",fname="test4")

def test5():
    'this passes'
    replicate_id_bug(sbml_sid="sbml",model_sid="model",unitdef_sid="unitdef",unit_sid=None,fname="test5")
