#!/usr/bin/env python3

'''
initial attempt at creating an SBML API using modelspec
https://github.com/combine-org/compbiolibs/issues/28

based on sbml.level-3.version-2.core.release-2.pdf
'''

import json
import yaml

import modelspec
from modelspec import field, instance_of, optional
from modelspec.base_types import Base
from typing import List


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

def replicate_id_bug():
    '''
    minimal replication of the missing 'id' error
    '''

    sbml_doc = SBML(id="sbml1")
    model = Model(id="model1")
    sbml_doc.model = model

    #unit definition list
    unitDef = UnitDefinition(id="metres_per_second")
    unit1 = Unit()
    unit2 = Unit(id="unit2")
    unitDef.listOfUnits.append(unit1)
    unitDef.listOfUnits.append(unit2)
    model.listOfUnitDefinitions.append(unitDef)

    path = "complete_example"

    print(sbml_doc.id)

    sbml_doc.to_json_file(f"{path}.json")
    sbml_doc.to_yaml_file(f"{path}.yaml")
    sbml_doc.to_bson_file(f"{path}.bson")

    print(sbml_doc.id)

if __name__ == "__main__":

    replicate_id_bug()
