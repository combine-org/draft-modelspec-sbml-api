#!/usr/bin/env python3

'''
initial attempt at creating an SBML API using modelspec
https://github.com/combine-org/compbiolibs/issues/28

based on sbml.level-3.version-2.core.release-2.pdf
'''

import json
import yaml

from sbml32spec import *

def test_sbml_empty():
    'empty sbml with only defaults'

    sbml_doc = SBML()

    assert sbml_doc.sid        == None
    assert sbml_doc.name       == None
    assert sbml_doc.metaid     == None
    assert sbml_doc.sboTerm    == None
    assert sbml_doc.notes      == None
    assert sbml_doc.annotation == None

    assert sbml_doc.xmlns   == "http://www.sbml.org/sbml/level3/version2/core"
    assert sbml_doc.level   == "3"
    assert sbml_doc.version == "2"

    assert sbml_doc.model   == None

def test_sbml_sid():
    'test validation of SBML.sid values'

    #valid values should be accepted
    for value in ["abc_123","A1B2C3_","_A_BC321"]:
        SBML(sid=value)

    #invalid values should throw a ValueError
    for value in ["123","A.1","z:"]:
        try:
            SBML(sid=value)
            raise Exception(f'invalid value was accepted: {value}')
        except ValueError:
            pass

def test_complete_example():
    '''
    aiming to have at least one of every item type
    not fully implemented yet
    '''

    #a minimal exmaple xhtml document
    content='''
    <html xmlns="http://www.w3.org/TR/xhtml1/strict">
        <head>
            <title>A Small Document</title>
        </head>
        <body>
            <p>A simple page!</p>
        </body>
    </html>'''

    notes = Notes(content=content)

    annotation = "<thing>minimum xml</thing>"

    sbml_doc = SBML(sid="sbml1",name="my name is sbml doc",metaid="zuckerberg",sboTerm="SBO:1234567",notes=notes,annotation=annotation)
    model = Model(sid="model1")
    sbml_doc.model = model

    #function definition list
    content = '<math> <lambda> <bvar><ci> x </ci></bvar> <apply> <power/> <ci> x </ci> <cn sbml:units="dimensionless"> 3 </cn> </apply> </lambda> </math>'
    math = Math(content=content)
    funcDef = FunctionDefinition(sid="funcdef1",math=math)
    model.listOfFunctionDefinitions.append(funcDef)

    #unit definition list
    unitDef = UnitDefinition(sid="metres_per_second")
    unit1 = Unit(kind="metre")
    unit2 = Unit(kind="second",exponent=-1.0)
    unitDef.listOfUnits.append(unit1)
    unitDef.listOfUnits.append(unit2)
    model.listOfUnitDefinitions.append(unitDef)

    #compartment list
    compartment = Compartment(sid="compartment1",spatialDimensions=3.0,size=2.798,constant=True)
    model.listOfCompartments.append(compartment)

    #species list
    species = Species(sid="species1",compartment="compartment1",hasOnlySubstanceUnits=False,boundaryCondition=False,constant=False)
    model.listOfSpecies.append(species)
    
    #parameter list
    parameter = Parameter(sid="parameter1",value=1.2345,units="meters_per_second",constant=False)
    model.listOfParameters.append(parameter)

    #initial assignment
    initialAssignment = InitialAssignment(sid="initialAssignment1",symbol="parameter1")
    model.listOfInitialAssignments.append(initialAssignment)

    path = "complete_example"

    sbml_doc.to_json_file(f"{path}.json")
    sbml_doc.to_yaml_file(f"{path}.yaml")
    sbml_doc.to_bson_file(f"{path}.bson")
    #sbml_doc.to_xml_file(f"{path}.xml")

    open(f"{path}.docs.md", "w").write(sbml_doc.generate_documentation(format="markdown"))
    open(f"{path}.docs.rst", "w").write(sbml_doc.generate_documentation(format="rst"))

    doc_dict = sbml_doc.generate_documentation(format="dict")
    open(f"{path}.docs.json", "w").write(json.dumps(doc_dict, indent=4))
    open(f"{path}.docs.yaml", "w").write(yaml.dump(doc_dict, indent=4, sort_keys=False))

if __name__ == "__main__":

    test_sbml_empty()
    test_sbml_sid()
    test_complete_example()
