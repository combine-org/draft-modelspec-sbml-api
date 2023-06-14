====
SBML
====
The top-level SBML container implementing SBML 3.2. See sbml.level-3.version-2.core.release-2.pdf section 4.
http://www.sbml.org/sbml/level3/version2/core

**Allowed parameters**

===============  =====================================  ========================================
Allowed field    Data Type                              Description
===============  =====================================  ========================================
**id**           str                                    SId optional
**name**         str                                    string optional
**metaid**       str                                    XML ID optional
**sboTerm**      str                                    SBOTerm optional
**notes**        str                                    XHTML 1.0 optional
**annotation**   str                                    XML content optional
**level**        str                                    SBML level used   (should be fixed to 3)
**version**      str                                    SBML version used (should be fixed to 2)
**model**        `<class '__main__.Model'> <#model>`__  Optional model
===============  =====================================  ========================================

=====
Model
=====
The model

**Allowed parameters**

====================  ===========  ==========================
Allowed field         Data Type    Description
====================  ===========  ==========================
**id**                str          The id of the model
**sboTerm**           str          Optional sboTerm
**substanceUnits**    str          Optional substance units
**timeUnits**         str          Optional time units
**volumeUnits**       str          Optional volume units
**areaUnits**         str          Optional area units
**lengthUnits**       str          Optional length units
**extentUnits**       str          Optional extent units
**conversionFactor**  str          Optional conversion factor
====================  ===========  ==========================

**Allowed children**

=============================  ================  =============
Allowed child                  Data Type         Description
=============================  ================  =============
**listOfFunctionDefinitions**  `List <#list>`__
**listOfUnitDefinitions**      `List <#list>`__
**listOfCompartments**         `List <#list>`__
**listOfSpecies**              `List <#list>`__
**listOfParameters**           `List <#list>`__
**listOfInitialAssignments**   `List <#list>`__
**listOfRules**                `List <#list>`__
=============================  ================  =============

==================
FunctionDefinition
==================
A function definition using MathML

**Allowed parameters**

===============  ===========  ============================================================================
Allowed field    Data Type    Description
===============  ===========  ============================================================================
**id**           str          The id of the function
**math**         str          Optional function definition using MathML http://www.w3.org/1998/Math/MathML
**sboTerm**      str          Optional sboTerm
===============  ===========  ============================================================================

==============
UnitDefinition
==============
A unit definition

**Allowed parameters**

===============  ===========  =============================
Allowed field    Data Type    Description
===============  ===========  =============================
**id**           str          The id of the unit definition
===============  ===========  =============================

**Allowed children**

===============  ================  ============================================
Allowed child    Data Type         Description
===============  ================  ============================================
**listOfUnits**  `List <#list>`__  List of units used to compose the definition
===============  ================  ============================================

====
Unit
====
A unit used to compose a unit definition. unit = (multiplier x 10^scale x kind)^exponent

**Allowed parameters**

===============  ===========  =======================================================================
Allowed field    Data Type    Description
===============  ===========  =======================================================================
**kind**         str          base unit (base or derived SI units only, see Table 2 of the SBML spec)
**exponent**     str          double
**scale**        str          integer
**multiplier**   str          double
===============  ===========  =======================================================================

===========
Compartment
===========
A compartment

**Allowed parameters**

=====================  ===========  =================================================
Allowed field          Data Type    Description
=====================  ===========  =================================================
**id**                 str          The id of the compartment
**constant**           bool         whether size is fixed
**sboTerm**            str          optional sboTerm
**spatialDimensions**  float        eg 3 for three dimensional space etc
**size**               float        initial size of compartment
**units**              str          units being used to define the compartment's size
=====================  ===========  =================================================

=======
Species
=======
A species: entities of the same kind participating in reactions within a specific compartment

**Allowed parameters**

=========================  ===========  =====================
Allowed field              Data Type    Description
=========================  ===========  =====================
**id**                     str          The id of the species
**compartment**            str          SIdRef
**hasOnlySubstanceUnits**  bool         boolean
**boundaryCondition**      bool         boolean
**constant**               bool         boolean
**initialAmount**          float        double optional
**initialConcentration**   float        double optional
**substanceUnits**         str          UnitSIdRef optional
**conversionFactor**       str          SIdRef optional
**sboTerm**                str          optional sboTerm
=========================  ===========  =====================

=========
Parameter
=========
A parameter

**Allowed parameters**

===============  ===========  ===================
Allowed field    Data Type    Description
===============  ===========  ===================
**id**           str          SId required
**constant**     bool         boolean
**sboTerm**      str          optional sboTerm
**value**        float        double optional
**units**        str          UnitSIdRef optional
===============  ===========  ===================

=================
InitialAssignment
=================
An initial assignment

**Allowed parameters**

===============  ===========  ================
Allowed field    Data Type    Description
===============  ===========  ================
**symbol**       str          SIdRef required
**id**           str          SId optional
**math**         str          MathML optional
**sboTerm**      str          sboTerm optional
===============  ===========  ================

====
Rule
====
A rule, either algebraic, assignment or rate

