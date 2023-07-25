#!/usr/bin/env python3

'''
initial attempt at creating an SBML API using modelspec
https://github.com/combine-org/compbiolibs/issues/28

based on sbml.level-3.version-2.core.release-2.pdf
'''

import modelspec
from modelspec import field, instance_of, optional
from modelspec.base_types import Base
from typing import List

@modelspec.define
class SBase(Base):
    """
    Abstract base class for all SBML objects

    Args:
        id:      SId optional
        name:    string optional
        metaid:  XML ID optional
        sboTerm: SBOTerm optional

        notes:      XHTML 1.0 optional
        annotation: XML content optional
    """

    id:      str = field(default=None,validator=optional(instance_of(str)))
    name:    str = field(default=None,validator=optional(instance_of(str)))
    metaid:  str = field(default=None,validator=optional(instance_of(str)))
    sboTerm: str = field(default=None,validator=optional(instance_of(str)))

    notes:      str = field(default=None,validator=optional(instance_of(str)))
    annotation: str = field(default=None,validator=optional(instance_of(str)))

@modelspec.define
class Event(SBase):
    useValuesFromTriggerTime: bool = field(default=None,validator=instance_of(bool))
    trigger:  Trigger = field(default=None, validator=optional(instance_of(Trigger)))
    priority: Priority = field(default=None, validator=optional(instance_of(Priority)))
    delay:    Delay = field(default=None, validator=optional(instance_of(Delay)))
    listOfEventAssignments: List[EventAssignments]   = field(factory=list)

@modelspec.define
class SimpleSpeciesReference(SBase):
    """
    Base class used by SpeciesReference and ModifierSpeciesReference

    Args:
        species: SIdRef
    """

    species: str = field(default=None,validator=instance_of(str))

@modelspec.define
class ModifierSpeciesReference(SimpleSpeciesReference):
    ''

@modelspec.define
class SpeciesReference(SimpleSpeciesReference):
    """
    Args:
        stoichiometry: double optional
        constant: boolean
    """

    stoichiometry: float = field(default=None,validator=optional(instance_of(float)))
    constant:      bool = field(default=None,validator=instance_of(bool))

@modelspec.define
class LocalParameter(SBase):
    """
    Args:
        units: UnitSIdRef optional
    """

    value: float = field(default=None,validator=optional(instance_of(float)))
    units: str = field(default=None,validator=optional(instance_of(str)))

@modelspec.define
class KineticLaw(SBase):
    """
    """

    math: str = field(default=None,validator=optional(instance_of(str)))

    listOfLocalParameters:           List[LocalParameter]   = field(factory=list)

@modelspec.define
class Reaction(SBase):
    """
    A model reaction

    Args:
        reversible: boolean
        compartment: SIdRef optional
    """

    reversible:   bool = field(default=None,validator=instance_of(bool))
    compartment:  str = field(default=None,validator=optional(instance_of(str)))

    listOfReactants:           List[SpeciesReference]           = field(factory=list)
    listOfProducts:            List[SpeciesReference]           = field(factory=list)
    listOfModifiers:           List[ModifierSpeciesReference]   = field(factory=list)

    kineticLaw:  KineticLaw = field(default=None, validator=optional(instance_of(KineticLaw)))

@modelspec.define
class Constraint(SBase):
    """
    A model constraint

    Args:
        math:    MathML optional
        message: XHTML 1.0 optional
    """

    math:    str = field(default=None,validator=optional(instance_of(str)))
    message: str = field(default=None,validator=optional(instance_of(str)))

@modelspec.define
class Rule(SBase):
    """
    A rule, either algebraic, assignment or rate

    Args:
        math: MathML optional
    """

    math: str = field(default=None,validator=optional(instance_of(str)))

@modelspec.define
class AlgebraicRule(Rule):
    """
    An algebraic rule
    """

@modelspec.define
class AssignmentRule(Rule):
    """
    An assignment rule

    Args:
        variable: SIdRef required
    """

    variable: str = field(default=None,validator=instance_of(str))

@modelspec.define
class RateRule(Rule):
    """
    A rate rule

    Args:
        variable: SIdRef required
    """

    variable: str = field(default=None,validator=instance_of(str))

@modelspec.define
class InitialAssignment(SBase):
    """
    An initial assignment

    Args:
        symbol: SIdRef required
        math: MathML optional
    """

    symbol: str = field(default=None,validator=instance_of(str))
    math: str = field(default=None,validator=optional(instance_of(str)))

@modelspec.define
class Parameter(SBase):
    """
    A parameter

    Args:
        value: double optional
        units: UnitSIdRef optional
        constant: boolean
    """

    constant: bool = field(default=None,validator=instance_of(bool))

    value: float = field(default=None,validator=optional(instance_of(float)))
    units: str = field(default=None,validator=optional(instance_of(str)))

@modelspec.define
class Species(SBase):
    """
    A species: entities of the same kind participating in reactions within a specific compartment

    Args:
        compartment: SIdRef
        initialAmount: double optional
        initialConcentration: double optional
        substanceUnits: UnitSIdRef optional
        hasOnlySubstanceUnits: boolean
        boundaryCondition: boolean
        constant: boolean
        conversionFactor: SIdRef optional
    """

    compartment: str = field(default=None,validator=instance_of(str))
    hasOnlySubstanceUnits: bool = field(default=None,validator=instance_of(bool))
    boundaryCondition: bool = field(default=None,validator=instance_of(bool))
    constant: bool = field(default=None,validator=instance_of(bool))

    initialAmount: float = field(default=None, validator=optional(instance_of(float)))
    initialConcentration: float = field(default=None, validator=optional(instance_of(float)))
    substanceUnits: str = field(default=None, validator=optional(instance_of(str)))
    conversionFactor: str = field(default=None, validator=optional(instance_of(str)))

@modelspec.define
class Compartment(SBase):
    """
    A compartment

    Args:
        spatialDimensions: eg 3 for three dimensional space etc
        size: initial size of compartment
        units: units being used to define the compartment's size
        constant: whether size is fixed
    """

    constant: bool = field(default=None,validator=instance_of(bool))

    spatialDimensions: float = field(default=None,validator=optional(instance_of(float)))
    size: float = field(default=None,validator=optional(instance_of(float)))
    units: str = field(default=None,validator=optional(instance_of(str)))

@modelspec.define
class Unit(SBase):
    """
    A unit used to compose a unit definition.
    unit = (multiplier x 10^scale x kind)^exponent

    Args:
        kind: base unit (base or derived SI units only, see Table 2 of the SBML spec)
        exponent: double
        scale: integer
        multiplier: double
    """

    kind:       str = field(default=None,validator=instance_of(str))
    exponent:   str = field(default=1.0, validator=instance_of(float))
    scale:      str = field(default=0,   validator=instance_of(int))
    multiplier: str = field(default=1.0, validator=instance_of(float))

@modelspec.define
class UnitDefinition(SBase):
    """
    A unit definition

    Args:
        listOfUnits: List of units used to compose the definition
    """

    listOfUnits: List[Unit] = field(factory=list)

@modelspec.define
class FunctionDefinition(SBase):
    """
    A function definition using MathML

    Args:
        math: Optional function definition using MathML http://www.w3.org/1998/Math/MathML
    """

    math: str = field(default=None, validator=optional(instance_of(str)))

@modelspec.define
class Model(SBase):
    """
    The model

    Args:
        substanceUnits:   Optional substance units
        timeUnits:        Optional time units
        volumeUnits:      Optional volume units
        areaUnits:        Optional area units
        lengthUnits:      Optional length units
        extentUnits:      Optional extent units
        conversionFactor: Optional conversion factor
    """

    substanceUnits:   str = field(default=None, validator=optional(instance_of(str)))
    timeUnits:        str = field(default=None, validator=optional(instance_of(str)))
    volumeUnits:      str = field(default=None, validator=optional(instance_of(str)))
    areaUnits:        str = field(default=None, validator=optional(instance_of(str)))
    lengthUnits:      str = field(default=None, validator=optional(instance_of(str)))
    extentUnits:      str = field(default=None, validator=optional(instance_of(str)))
    conversionFactor: str = field(default=None, validator=optional(instance_of(str)))

    listOfFunctionDefinitions: List[FunctionDefinition] = field(factory=list)
    listOfUnitDefinitions:     List[UnitDefinition]     = field(factory=list)
    listOfCompartments:        List[Compartment]        = field(factory=list)
    listOfSpecies:             List[Species]            = field(factory=list)
    listOfParameters:          List[Parameter]          = field(factory=list)
    listOfInitialAssignments:  List[InitialAssignment]  = field(factory=list)
    listOfRules:               List[Rule]               = field(factory=list)
    listOfConstraints:         List[Constraint]         = field(factory=list)
    listOfReactions:           List[Reaction]           = field(factory=list)
    listOfEvents:              List[Event]              = field(factory=list)

@modelspec.define
class SBML(SBase):
    """
    The top-level SBML container implementing SBML 3.2.
    See sbml.level-3.version-2.core.release-2.pdf section 4.
    http://www.sbml.org/sbml/level3/version2/core

    Args:
        level:   SBML level used   (should be fixed to 3)
        version: SBML version used (should be fixed to 2)

        model:   Optional model
    """

    level:   str = field(default="3",validator=instance_of(str))
    version: str = field(default="2",validator=instance_of(str))

    model: Model = field(default=None, validator=optional(instance_of(Model)))

if __name__ == "__main__":
    sbml_doc = SBML(id="sbml_example")
    print(sbml_doc.id)
    model = Model(id="model1")
    sbml_doc.model = model

    #function definition list
    funcDef = FunctionDefinition(id="my_func")
    funcDef.math = \
    '''<math xmlns="http://www.w3.org/1998/Math/MathML"> <apply> <eq/> <apply> <plus/> <cn>2</cn> <cn>2</cn> </apply> <cn>4</cn> </apply> </math>'''
    model.listOfFunctionDefinitions.append(funcDef)

    #unit definition list
    unitDef = UnitDefinition(id="metres_per_second")
    unit1 = Unit(kind="metre")
    unit2 = Unit(kind="second",exponent=-1.0)
    unitDef.listOfUnits.append(unit1)
    unitDef.listOfUnits.append(unit2)
    model.listOfUnitDefinitions.append(unitDef)

    #compartment list
    compartment = Compartment(id="compartment1",spatialDimensions=3.0,size=2.798,constant=True)
    model.listOfCompartments.append(compartment)

    #species list
    species = Species(id="species1",compartment="compartment1",hasOnlySubstanceUnits=False,boundaryCondition=False,constant=False)
    model.listOfSpecies.append(species)
    
    #parameter list
    parameter = Parameter(id="parameter1",value=1.2345,units="meters_per_second",constant=False)
    model.listOfParameters.append(parameter)

    #initial assignment
    initialAssignment = InitialAssignment(id="initialAssignment1",symbol="parameter1")
    model.listOfInitialAssignments.append(initialAssignment)

    print(sbml_doc)
    print(sbml_doc.id)

    sbml_doc.to_json_file("%s.json" % sbml_doc.id)
    sbml_doc.to_yaml_file("%s.yaml" % sbml_doc.id)
    sbml_doc.to_bson_file("%s.bson" % sbml_doc.id)
    # sbml_doc.to_xml_file("%s.xml"%sbml_doc.id)

    print(" >> Full document details in YAML format:\n")

    print(sbml_doc.to_yaml())

    doc_md = sbml_doc.generate_documentation(format="markdown")

    with open("SBML3.md", "w") as d:
        d.write(doc_md)

    doc_rst = sbml_doc.generate_documentation(format="rst")

    with open("SBML3.rst", "w") as d:
        d.write(doc_rst)

    print("\n  >> Generating specification in dict form...")
    doc_dict = sbml_doc.generate_documentation(format="dict")

    import json
    import yaml

    with open("SBML3.specification.json", "w") as d:
        d.write(json.dumps(doc_dict, indent=4))

    print("  >> Generating specification in YAML...\n")

    with open("SBML3.specification.yaml", "w") as d:
        yy = yaml.dump(doc_dict, indent=4, sort_keys=False)
        print(yy)
        d.write(yy)
