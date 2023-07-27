====
SBML
====
The top-level SBML container implementing SBML 3.2. See sbml.level-3.version-2.core.release-2.pdf section 4.
http://www.sbml.org/sbml/level3/version2/core

**Allowed parameters**

===============  =======================================  ================================================================
Allowed field    Data Type                                Description
===============  =======================================  ================================================================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**xmlns**        str                                      string, fixed to "http://www.sbml.org/sbml/level3/version2/core"
**level**        str                                      SBML level, fixed to 3
**version**      str                                      SBML version, fixed to 2
**model**        `<class 'sbml32spec.Model'> <#model>`__  Optional model
===============  =======================================  ================================================================

=====
Notes
=====
**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

=====
Model
=====
The model

**Allowed parameters**

====================  =======================================  ====================
Allowed field         Data Type                                Description
====================  =======================================  ====================
**sid**               str                                      SId optional
**name**              str                                      string optional
**metaid**            str                                      XML ID optional
**sboTerm**           str                                      SBOTerm optional
**notes**             `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**        str                                      XML content optional
**substanceUnits**    str                                      UnitSIdRef optional
**timeUnits**         str                                      UnitSIdRef optional
**volumeUnits**       str                                      UnitSIdRef optional
**areaUnits**         str                                      UnitSIdRef optional
**lengthUnits**       str                                      UnitSIdRef optional
**extentUnits**       str                                      UnitSIdRef optional
**conversionFactor**  str                                      SIdRef optional
====================  =======================================  ====================

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
**listOfConstraints**          `List <#list>`__
**listOfReactions**            `List <#list>`__
**listOfEvents**               `List <#list>`__
=============================  ================  =============

=====
Notes
=====
**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

==================
FunctionDefinition
==================
A function definition using MathML

**Allowed parameters**

===============  =======================================  ===================================
Allowed field    Data Type                                Description
===============  =======================================  ===================================
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**sid**          str                                      SId optional
**math**         `<class 'sbml32spec.Math'> <#math>`__    MathML function definition optional
===============  =======================================  ===================================

=====
Notes
=====
**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

====
Math
====
**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

==============
UnitDefinition
==============
A unit definition

**Allowed parameters**

===============  =======================================  ====================
Allowed field    Data Type                                Description
===============  =======================================  ====================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
===============  =======================================  ====================

**Allowed children**

===============  ================  ============================================
Allowed child    Data Type         Description
===============  ================  ============================================
**listOfUnits**  `List <#list>`__  List of units used to compose the definition
===============  ================  ============================================

=====
Notes
=====
**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

====
Unit
====
A unit used to compose a unit definition. unit = (multiplier x 10^scale x kind)^exponent

**Allowed parameters**

===============  =======================================  =======================================================================
Allowed field    Data Type                                Description
===============  =======================================  =======================================================================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**kind**         str                                      base unit (base or derived SI units only, see Table 2 of the SBML spec)
**exponent**     str                                      double
**scale**        str                                      integer
**multiplier**   str                                      double
===============  =======================================  =======================================================================

=====
Notes
=====
**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

===========
Compartment
===========
A compartment

**Allowed parameters**

=====================  =======================================  =================================================
Allowed field          Data Type                                Description
=====================  =======================================  =================================================
**sid**                str                                      SId optional
**name**               str                                      string optional
**metaid**             str                                      XML ID optional
**sboTerm**            str                                      SBOTerm optional
**notes**              `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**         str                                      XML content optional
**constant**           bool                                     whether size is fixed
**spatialDimensions**  float                                    eg 3 for three dimensional space etc
**size**               float                                    initial size of compartment
**units**              str                                      units being used to define the compartment's size
=====================  =======================================  =================================================

=====
Notes
=====
**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

=======
Species
=======
A species: entities of the same kind participating in reactions within a specific compartment

**Allowed parameters**

=========================  =======================================  ====================
Allowed field              Data Type                                Description
=========================  =======================================  ====================
**sid**                    str                                      SId optional
**name**                   str                                      string optional
**metaid**                 str                                      XML ID optional
**sboTerm**                str                                      SBOTerm optional
**notes**                  `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**             str                                      XML content optional
**compartment**            str                                      SIdRef
**hasOnlySubstanceUnits**  bool                                     boolean
**boundaryCondition**      bool                                     boolean
**constant**               bool                                     boolean
**initialAmount**          float                                    double optional
**initialConcentration**   float                                    double optional
**substanceUnits**         str                                      UnitSIdRef optional
**conversionFactor**       str                                      SIdRef optional
=========================  =======================================  ====================

=====
Notes
=====
**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

=========
Parameter
=========
A parameter

**Allowed parameters**

===============  =======================================  ====================
Allowed field    Data Type                                Description
===============  =======================================  ====================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**constant**     bool                                     boolean
**value**        float                                    double optional
**units**        str                                      UnitSIdRef optional
===============  =======================================  ====================

=====
Notes
=====
**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

=================
InitialAssignment
=================
An initial assignment

**Allowed parameters**

===============  =======================================  ====================
Allowed field    Data Type                                Description
===============  =======================================  ====================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**symbol**       str                                      SIdRef required
**math**         str                                      MathML optional
===============  =======================================  ====================

=====
Notes
=====
**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

====
Rule
====
A rule, either algebraic, assignment or rate

**Allowed parameters**

===============  =======================================  ====================
Allowed field    Data Type                                Description
===============  =======================================  ====================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**math**         str                                      MathML optional
===============  =======================================  ====================

=====
Notes
=====
**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

==========
Constraint
==========
A model constraint

**Allowed parameters**

===============  =======================================  ====================
Allowed field    Data Type                                Description
===============  =======================================  ====================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**math**         str                                      MathML optional
**message**      str                                      XHTML 1.0 optional
===============  =======================================  ====================

=====
Notes
=====
**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

========
Reaction
========
A model reaction

**Allowed parameters**

===============  =================================================  ====================
Allowed field    Data Type                                          Description
===============  =================================================  ====================
**sid**          str                                                SId optional
**name**         str                                                string optional
**metaid**       str                                                XML ID optional
**sboTerm**      str                                                SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__            XHTML 1.0 optional
**annotation**   str                                                XML content optional
**reversible**   bool                                               boolean
**compartment**  str                                                SIdRef optional
**kineticLaw**   `<class 'sbml32spec.KineticLaw'> <#kineticlaw>`__
===============  =================================================  ====================

**Allowed children**

===================  ================  =============
Allowed child        Data Type         Description
===================  ================  =============
**listOfReactants**  `List <#list>`__
**listOfProducts**   `List <#list>`__
**listOfModifiers**  `List <#list>`__
===================  ================  =============

=====
Notes
=====
**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

==========
KineticLaw
==========
    

**Allowed parameters**

===============  =======================================  ====================
Allowed field    Data Type                                Description
===============  =======================================  ====================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**math**         str
===============  =======================================  ====================

**Allowed children**

=========================  ================  =============
Allowed child              Data Type         Description
=========================  ================  =============
**listOfLocalParameters**  `List <#list>`__
=========================  ================  =============

=====
Notes
=====
**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

==============
LocalParameter
==============
**Allowed parameters**

===============  =======================================  ====================
Allowed field    Data Type                                Description
===============  =======================================  ====================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**value**        float
**units**        str                                      UnitSIdRef optional
===============  =======================================  ====================

=====
Notes
=====
**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

================
SpeciesReference
================
**Allowed parameters**

=================  =======================================  ====================
Allowed field      Data Type                                Description
=================  =======================================  ====================
**sid**            str                                      SId optional
**name**           str                                      string optional
**metaid**         str                                      XML ID optional
**sboTerm**        str                                      SBOTerm optional
**notes**          `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**     str                                      XML content optional
**species**        str                                      SIdRef
**stoichiometry**  float                                    double optional
**constant**       bool                                     boolean
=================  =======================================  ====================

=====
Notes
=====
**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

================
SpeciesReference
================
**Allowed parameters**

=================  =======================================  ====================
Allowed field      Data Type                                Description
=================  =======================================  ====================
**sid**            str                                      SId optional
**name**           str                                      string optional
**metaid**         str                                      XML ID optional
**sboTerm**        str                                      SBOTerm optional
**notes**          `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**     str                                      XML content optional
**species**        str                                      SIdRef
**stoichiometry**  float                                    double optional
**constant**       bool                                     boolean
=================  =======================================  ====================

=====
Notes
=====
**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

========================
ModifierSpeciesReference
========================
**Allowed parameters**

===============  =======================================  ====================
Allowed field    Data Type                                Description
===============  =======================================  ====================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**species**      str                                      SIdRef
===============  =======================================  ====================

=====
Notes
=====
**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

=====
Event
=====
**Allowed parameters**

============================  =============================================  ====================
Allowed field                 Data Type                                      Description
============================  =============================================  ====================
**sid**                       str                                            SId optional
**name**                      str                                            string optional
**metaid**                    str                                            XML ID optional
**sboTerm**                   str                                            SBOTerm optional
**notes**                     `<class 'sbml32spec.Notes'> <#notes>`__        XHTML 1.0 optional
**annotation**                str                                            XML content optional
**useValuesFromTriggerTime**  bool
**trigger**                   `<class 'sbml32spec.Trigger'> <#trigger>`__
**priority**                  `<class 'sbml32spec.Priority'> <#priority>`__
**delay**                     `<class 'sbml32spec.Delay'> <#delay>`__
============================  =============================================  ====================

**Allowed children**

==========================  ================  =============
Allowed child               Data Type         Description
==========================  ================  =============
**listOfEventAssignments**  `List <#list>`__
==========================  ================  =============

=====
Notes
=====
**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

=======
Trigger
=======
**Allowed parameters**

================  =======================================  ====================
Allowed field     Data Type                                Description
================  =======================================  ====================
**sid**           str                                      SId optional
**name**          str                                      string optional
**metaid**        str                                      XML ID optional
**sboTerm**       str                                      SBOTerm optional
**notes**         `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**    str                                      XML content optional
**initialValue**  bool
**persistent**    bool
**math**          str
================  =======================================  ====================

=====
Notes
=====
**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

========
Priority
========
**Allowed parameters**

===============  =======================================  ====================
Allowed field    Data Type                                Description
===============  =======================================  ====================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**math**         str
===============  =======================================  ====================

=====
Notes
=====
**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

=====
Delay
=====
**Allowed parameters**

===============  =======================================  ====================
Allowed field    Data Type                                Description
===============  =======================================  ====================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**math**         str
===============  =======================================  ====================

=====
Notes
=====
**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

===============
EventAssignment
===============
**Allowed parameters**

===============  =======================================  ====================
Allowed field    Data Type                                Description
===============  =======================================  ====================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        `<class 'sbml32spec.Notes'> <#notes>`__  XHTML 1.0 optional
**annotation**   str                                      XML content optional
**math**         str
**variable**     str                                      SIdRef
===============  =======================================  ====================

=====
Notes
=====
**Allowed parameters**

===============  ===========  =============
Allowed field    Data Type    Description
===============  ===========  =============
**xmlns**        str
**content**      str
===============  ===========  =============

