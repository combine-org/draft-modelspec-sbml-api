====
SBML
====
The top-level SBML container implementing SBML 3.2. See sbml.level-3.version-2.core.release-2.pdf section 4.
http://www.sbml.org/sbml/level3/version2/core

**Allowed parameters**

===============  =======================================  ========================
Allowed field    Data Type                                Description
===============  =======================================  ========================
**sid**          str                                      SId optional
**name**         str                                      string optional
**metaid**       str                                      XML ID optional
**sboTerm**      str                                      SBOTerm optional
**notes**        str                                      XHTML 1.0 optional
**annotation**   str                                      XML content optional
**level**        str                                      SBML level   (must be 3)
**version**      str                                      SBML version (must be 2)
**model**        `<class 'sbml32spec.Model'> <#model>`__  Optional model
===============  =======================================  ========================

=====
Model
=====
The model

**Allowed parameters**

====================  ===========  ==========================
Allowed field         Data Type    Description
====================  ===========  ==========================
**sid**               str          SId optional
**name**              str          string optional
**metaid**            str          XML ID optional
**sboTerm**           str          SBOTerm optional
**notes**             str          XHTML 1.0 optional
**annotation**        str          XML content optional
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
**listOfConstraints**          `List <#list>`__
**listOfReactions**            `List <#list>`__
**listOfEvents**               `List <#list>`__
=============================  ================  =============

==================
FunctionDefinition
==================
A function definition using MathML

**Allowed parameters**

===============  ===========  ============================================================================
Allowed field    Data Type    Description
===============  ===========  ============================================================================
**sid**          str          SId optional
**name**         str          string optional
**metaid**       str          XML ID optional
**sboTerm**      str          SBOTerm optional
**notes**        str          XHTML 1.0 optional
**annotation**   str          XML content optional
**math**         str          Optional function definition using MathML http://www.w3.org/1998/Math/MathML
===============  ===========  ============================================================================

==============
UnitDefinition
==============
A unit definition

**Allowed parameters**

===============  ===========  ====================
Allowed field    Data Type    Description
===============  ===========  ====================
**sid**          str          SId optional
**name**         str          string optional
**metaid**       str          XML ID optional
**sboTerm**      str          SBOTerm optional
**notes**        str          XHTML 1.0 optional
**annotation**   str          XML content optional
===============  ===========  ====================

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
**sid**          str          SId optional
**name**         str          string optional
**metaid**       str          XML ID optional
**sboTerm**      str          SBOTerm optional
**notes**        str          XHTML 1.0 optional
**annotation**   str          XML content optional
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
**sid**                str          SId optional
**name**               str          string optional
**metaid**             str          XML ID optional
**sboTerm**            str          SBOTerm optional
**notes**              str          XHTML 1.0 optional
**annotation**         str          XML content optional
**constant**           bool         whether size is fixed
**spatialDimensions**  float        eg 3 for three dimensional space etc
**size**               float        initial size of compartment
**units**              str          units being used to define the compartment's size
=====================  ===========  =================================================

=======
Species
=======
A species: entities of the same kind participating in reactions within a specific compartment

**Allowed parameters**

=========================  ===========  ====================
Allowed field              Data Type    Description
=========================  ===========  ====================
**sid**                    str          SId optional
**name**                   str          string optional
**metaid**                 str          XML ID optional
**sboTerm**                str          SBOTerm optional
**notes**                  str          XHTML 1.0 optional
**annotation**             str          XML content optional
**compartment**            str          SIdRef
**hasOnlySubstanceUnits**  bool         boolean
**boundaryCondition**      bool         boolean
**constant**               bool         boolean
**initialAmount**          float        double optional
**initialConcentration**   float        double optional
**substanceUnits**         str          UnitSIdRef optional
**conversionFactor**       str          SIdRef optional
=========================  ===========  ====================

=========
Parameter
=========
A parameter

**Allowed parameters**

===============  ===========  ====================
Allowed field    Data Type    Description
===============  ===========  ====================
**sid**          str          SId optional
**name**         str          string optional
**metaid**       str          XML ID optional
**sboTerm**      str          SBOTerm optional
**notes**        str          XHTML 1.0 optional
**annotation**   str          XML content optional
**constant**     bool         boolean
**value**        float        double optional
**units**        str          UnitSIdRef optional
===============  ===========  ====================

=================
InitialAssignment
=================
An initial assignment

**Allowed parameters**

===============  ===========  ====================
Allowed field    Data Type    Description
===============  ===========  ====================
**sid**          str          SId optional
**name**         str          string optional
**metaid**       str          XML ID optional
**sboTerm**      str          SBOTerm optional
**notes**        str          XHTML 1.0 optional
**annotation**   str          XML content optional
**symbol**       str          SIdRef required
**math**         str          MathML optional
===============  ===========  ====================

====
Rule
====
A rule, either algebraic, assignment or rate

**Allowed parameters**

===============  ===========  ====================
Allowed field    Data Type    Description
===============  ===========  ====================
**sid**          str          SId optional
**name**         str          string optional
**metaid**       str          XML ID optional
**sboTerm**      str          SBOTerm optional
**notes**        str          XHTML 1.0 optional
**annotation**   str          XML content optional
**math**         str          MathML optional
===============  ===========  ====================

==========
Constraint
==========
A model constraint

**Allowed parameters**

===============  ===========  ====================
Allowed field    Data Type    Description
===============  ===========  ====================
**sid**          str          SId optional
**name**         str          string optional
**metaid**       str          XML ID optional
**sboTerm**      str          SBOTerm optional
**notes**        str          XHTML 1.0 optional
**annotation**   str          XML content optional
**math**         str          MathML optional
**message**      str          XHTML 1.0 optional
===============  ===========  ====================

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
**notes**        str                                                XHTML 1.0 optional
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

==========
KineticLaw
==========
    

**Allowed parameters**

===============  ===========  ====================
Allowed field    Data Type    Description
===============  ===========  ====================
**sid**          str          SId optional
**name**         str          string optional
**metaid**       str          XML ID optional
**sboTerm**      str          SBOTerm optional
**notes**        str          XHTML 1.0 optional
**annotation**   str          XML content optional
**math**         str
===============  ===========  ====================

**Allowed children**

=========================  ================  =============
Allowed child              Data Type         Description
=========================  ================  =============
**listOfLocalParameters**  `List <#list>`__
=========================  ================  =============

==============
LocalParameter
==============
**Allowed parameters**

===============  ===========  ====================
Allowed field    Data Type    Description
===============  ===========  ====================
**sid**          str          SId optional
**name**         str          string optional
**metaid**       str          XML ID optional
**sboTerm**      str          SBOTerm optional
**notes**        str          XHTML 1.0 optional
**annotation**   str          XML content optional
**value**        float
**units**        str          UnitSIdRef optional
===============  ===========  ====================

================
SpeciesReference
================
**Allowed parameters**

=================  ===========  ====================
Allowed field      Data Type    Description
=================  ===========  ====================
**sid**            str          SId optional
**name**           str          string optional
**metaid**         str          XML ID optional
**sboTerm**        str          SBOTerm optional
**notes**          str          XHTML 1.0 optional
**annotation**     str          XML content optional
**species**        str          SIdRef
**stoichiometry**  float        double optional
**constant**       bool         boolean
=================  ===========  ====================

================
SpeciesReference
================
**Allowed parameters**

=================  ===========  ====================
Allowed field      Data Type    Description
=================  ===========  ====================
**sid**            str          SId optional
**name**           str          string optional
**metaid**         str          XML ID optional
**sboTerm**        str          SBOTerm optional
**notes**          str          XHTML 1.0 optional
**annotation**     str          XML content optional
**species**        str          SIdRef
**stoichiometry**  float        double optional
**constant**       bool         boolean
=================  ===========  ====================

========================
ModifierSpeciesReference
========================
**Allowed parameters**

===============  ===========  ====================
Allowed field    Data Type    Description
===============  ===========  ====================
**sid**          str          SId optional
**name**         str          string optional
**metaid**       str          XML ID optional
**sboTerm**      str          SBOTerm optional
**notes**        str          XHTML 1.0 optional
**annotation**   str          XML content optional
**species**      str          SIdRef
===============  ===========  ====================

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
**notes**                     str                                            XHTML 1.0 optional
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

=======
Trigger
=======
**Allowed parameters**

================  ===========  ====================
Allowed field     Data Type    Description
================  ===========  ====================
**sid**           str          SId optional
**name**          str          string optional
**metaid**        str          XML ID optional
**sboTerm**       str          SBOTerm optional
**notes**         str          XHTML 1.0 optional
**annotation**    str          XML content optional
**initialValue**  bool
**persistent**    bool
**math**          str
================  ===========  ====================

========
Priority
========
**Allowed parameters**

===============  ===========  ====================
Allowed field    Data Type    Description
===============  ===========  ====================
**sid**          str          SId optional
**name**         str          string optional
**metaid**       str          XML ID optional
**sboTerm**      str          SBOTerm optional
**notes**        str          XHTML 1.0 optional
**annotation**   str          XML content optional
**math**         str
===============  ===========  ====================

=====
Delay
=====
**Allowed parameters**

===============  ===========  ====================
Allowed field    Data Type    Description
===============  ===========  ====================
**sid**          str          SId optional
**name**         str          string optional
**metaid**       str          XML ID optional
**sboTerm**      str          SBOTerm optional
**notes**        str          XHTML 1.0 optional
**annotation**   str          XML content optional
**math**         str
===============  ===========  ====================

===============
EventAssignment
===============
**Allowed parameters**

===============  ===========  ====================
Allowed field    Data Type    Description
===============  ===========  ====================
**sid**          str          SId optional
**name**         str          string optional
**metaid**       str          XML ID optional
**sboTerm**      str          SBOTerm optional
**notes**        str          XHTML 1.0 optional
**annotation**   str          XML content optional
**math**         str
**variable**     str          SIdRef
===============  ===========  ====================

