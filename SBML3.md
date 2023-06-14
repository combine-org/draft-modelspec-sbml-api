## SBML
The top-level SBML container implementing SBML 3.2. See sbml.level-3.version-2.core.release-2.pdf section 4.
http://www.sbml.org/sbml/level3/version2/core

### Allowed parameters
<table>
  <tr>
    <td><b>id</b></td>
    <td>str</td>
    <td><i>     SId optional</i></td>
 </tr>


  <tr>
    <td><b>name</b></td>
    <td>str</td>
    <td><i>   string optional</i></td>
 </tr>


  <tr>
    <td><b>metaid</b></td>
    <td>str</td>
    <td><i> XML ID optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>SBOTerm optional</i></td>
 </tr>


  <tr>
    <td><b>notes</b></td>
    <td>str</td>
    <td><i>     XHTML 1.0 optional</i></td>
 </tr>


  <tr>
    <td><b>annotation</b></td>
    <td>str</td>
    <td><i>XML content optional</i></td>
 </tr>


  <tr>
    <td><b>level</b></td>
    <td>str</td>
    <td><i>  SBML level used   (should be fixed to 3)</i></td>
 </tr>


  <tr>
    <td><b>version</b></td>
    <td>str</td>
    <td><i>SBML version used (should be fixed to 2)</i></td>
 </tr>


  <tr>
    <td><b>model</b></td>
    <td><a href="#model">Model</a></td>
    <td><i>  Optional model</i></td>
 </tr>


</table>

## Model
The model

### Allowed parameters
<table>
  <tr>
    <td><b>id</b></td>
    <td>str</td>
    <td><i>              The id of the model</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>         Optional sboTerm</i></td>
 </tr>


  <tr>
    <td><b>substanceUnits</b></td>
    <td>str</td>
    <td><i>  Optional substance units</i></td>
 </tr>


  <tr>
    <td><b>timeUnits</b></td>
    <td>str</td>
    <td><i>       Optional time units</i></td>
 </tr>


  <tr>
    <td><b>volumeUnits</b></td>
    <td>str</td>
    <td><i>     Optional volume units</i></td>
 </tr>


  <tr>
    <td><b>areaUnits</b></td>
    <td>str</td>
    <td><i>       Optional area units</i></td>
 </tr>


  <tr>
    <td><b>lengthUnits</b></td>
    <td>str</td>
    <td><i>     Optional length units</i></td>
 </tr>


  <tr>
    <td><b>extentUnits</b></td>
    <td>str</td>
    <td><i>     Optional extent units</i></td>
 </tr>


  <tr>
    <td><b>conversionFactor</b></td>
    <td>str</td>
    <td><i>Optional conversion factor</i></td>
 </tr>


</table>

### Allowed children
<table>
  <tr>
    <td><b>listOfFunctionDefinitions</b></td>
    <td><a href="#list">List</a></td>
    <td><i></i></td>
  </tr>


  <tr>
    <td><b>listOfUnitDefinitions</b></td>
    <td><a href="#list">List</a></td>
    <td><i></i></td>
  </tr>


  <tr>
    <td><b>listOfCompartments</b></td>
    <td><a href="#list">List</a></td>
    <td><i></i></td>
  </tr>


  <tr>
    <td><b>listOfSpecies</b></td>
    <td><a href="#list">List</a></td>
    <td><i></i></td>
  </tr>


  <tr>
    <td><b>listOfParameters</b></td>
    <td><a href="#list">List</a></td>
    <td><i></i></td>
  </tr>


  <tr>
    <td><b>listOfInitialAssignments</b></td>
    <td><a href="#list">List</a></td>
    <td><i></i></td>
  </tr>


  <tr>
    <td><b>listOfRules</b></td>
    <td><a href="#list">List</a></td>
    <td><i></i></td>
  </tr>


</table>

## FunctionDefinition
A function definition using MathML

### Allowed parameters
<table>
  <tr>
    <td><b>id</b></td>
    <td>str</td>
    <td><i>The id of the function</i></td>
 </tr>


  <tr>
    <td><b>math</b></td>
    <td>str</td>
    <td><i>Optional function definition using MathML http://www.w3.org/1998/Math/MathML</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>Optional sboTerm</i></td>
 </tr>


</table>

## UnitDefinition
A unit definition

### Allowed parameters
<table>
  <tr>
    <td><b>id</b></td>
    <td>str</td>
    <td><i>The id of the unit definition</i></td>
 </tr>


</table>

### Allowed children
<table>
  <tr>
    <td><b>listOfUnits</b></td>
    <td><a href="#list">List</a></td>
    <td><i>List of units used to compose the definition</i></td>
  </tr>


</table>

## Unit
A unit used to compose a unit definition. unit = (multiplier x 10^scale x kind)^exponent

### Allowed parameters
<table>
  <tr>
    <td><b>kind</b></td>
    <td>str</td>
    <td><i>base unit (base or derived SI units only, see Table 2 of the SBML spec)</i></td>
 </tr>


  <tr>
    <td><b>exponent</b></td>
    <td>str</td>
    <td><i>double</i></td>
 </tr>


  <tr>
    <td><b>scale</b></td>
    <td>str</td>
    <td><i>integer</i></td>
 </tr>


  <tr>
    <td><b>multiplier</b></td>
    <td>str</td>
    <td><i>double</i></td>
 </tr>


</table>

## Compartment
A compartment

### Allowed parameters
<table>
  <tr>
    <td><b>id</b></td>
    <td>str</td>
    <td><i>The id of the compartment</i></td>
 </tr>


  <tr>
    <td><b>constant</b></td>
    <td>bool</td>
    <td><i>whether size is fixed</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>optional sboTerm</i></td>
 </tr>


  <tr>
    <td><b>spatialDimensions</b></td>
    <td>float</td>
    <td><i>eg 3 for three dimensional space etc</i></td>
 </tr>


  <tr>
    <td><b>size</b></td>
    <td>float</td>
    <td><i>initial size of compartment</i></td>
 </tr>


  <tr>
    <td><b>units</b></td>
    <td>str</td>
    <td><i>units being used to define the compartment's size</i></td>
 </tr>


</table>

## Species
A species: entities of the same kind participating in reactions within a specific compartment

### Allowed parameters
<table>
  <tr>
    <td><b>id</b></td>
    <td>str</td>
    <td><i>The id of the species</i></td>
 </tr>


  <tr>
    <td><b>compartment</b></td>
    <td>str</td>
    <td><i>SIdRef</i></td>
 </tr>


  <tr>
    <td><b>hasOnlySubstanceUnits</b></td>
    <td>bool</td>
    <td><i>boolean</i></td>
 </tr>


  <tr>
    <td><b>boundaryCondition</b></td>
    <td>bool</td>
    <td><i>boolean</i></td>
 </tr>


  <tr>
    <td><b>constant</b></td>
    <td>bool</td>
    <td><i>boolean</i></td>
 </tr>


  <tr>
    <td><b>initialAmount</b></td>
    <td>float</td>
    <td><i>double optional</i></td>
 </tr>


  <tr>
    <td><b>initialConcentration</b></td>
    <td>float</td>
    <td><i>double optional</i></td>
 </tr>


  <tr>
    <td><b>substanceUnits</b></td>
    <td>str</td>
    <td><i>UnitSIdRef optional</i></td>
 </tr>


  <tr>
    <td><b>conversionFactor</b></td>
    <td>str</td>
    <td><i>SIdRef optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>optional sboTerm</i></td>
 </tr>


</table>

## Parameter
A parameter

### Allowed parameters
<table>
  <tr>
    <td><b>id</b></td>
    <td>str</td>
    <td><i>SId required</i></td>
 </tr>


  <tr>
    <td><b>constant</b></td>
    <td>bool</td>
    <td><i>boolean</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>optional sboTerm</i></td>
 </tr>


  <tr>
    <td><b>value</b></td>
    <td>float</td>
    <td><i>double optional</i></td>
 </tr>


  <tr>
    <td><b>units</b></td>
    <td>str</td>
    <td><i>UnitSIdRef optional</i></td>
 </tr>


</table>

## InitialAssignment
An initial assignment

### Allowed parameters
<table>
  <tr>
    <td><b>symbol</b></td>
    <td>str</td>
    <td><i>SIdRef required</i></td>
 </tr>


  <tr>
    <td><b>id</b></td>
    <td>str</td>
    <td><i>SId optional</i></td>
 </tr>


  <tr>
    <td><b>math</b></td>
    <td>str</td>
    <td><i>MathML optional</i></td>
 </tr>


  <tr>
    <td><b>sboTerm</b></td>
    <td>str</td>
    <td><i>sboTerm optional</i></td>
 </tr>


</table>

## Rule
A rule, either algebraic, assignment or rate

