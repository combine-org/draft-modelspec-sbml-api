#!/usr/bin/env python3

'''
https://www.attrs.org/en/latest/examples.html:
"Keyword-only attributes allow subclasses to add attributes without default values, even if the base class defines attributes with default values
If you don’t set kw_only=True, then there is no valid attribute ordering, and you’ll get an error:
ValueError: No mandatory attributes allowed after an attribute with a default value or factory.
Attribute in question: Attribute(name='b', default=NOTHING, validator=None, repr=True, cmp=True, hash=None, init=True, converter=None, metadata=mappingproxy({}), type=int, kw_only=False)

below SubRule must be set to kw_only=True otherwise the above mentioned error occurs
this seems to be the preferred way to handle this case
my other workaround was to set default=None to everything
making the offending attribute optional does not fix the problem

the kw_only=True setting allows the below fragment of SBML spec to be parsed by python
but another error happens when objects are created using it, see test_sbase.py

in summary it looks like we need to keep using the default=None fix
rather than kw_only=True as the later only allows the spec to be defined without error
but seems not to allow kw_only attributes to be optional
it seems to effectively force them to be required unless default=None is also added
therefore kw_only option does not actually help out at all
and just using default=None seems to fix everything
'''

import modelspec
from modelspec import field, instance_of, optional
from modelspec.base_types import Base
from typing import List

@modelspec.define
class SBase(Base):
    id:      str = field(default=None,validator=optional(instance_of(str)))
    #name:    str = field(default=None,validator=optional(instance_of(str)))

@modelspec.define
class Rule(SBase):

    math: str = field(default=None,validator=optional(instance_of(str)))

@modelspec.define(kw_only=True)
class SubRule(Rule):

    variable: str = field(validator=instance_of(str))                         #error unless kw_only=True
    #variable: str = field(default=None,validator=instance_of(str))           #ok
    #variable: str = field(validator=optional(instance_of(str)))              #error unless kw_only=True
    #variable: str = field(default=None,validator=optional(instance_of(str))) #ok

def test_sbase():
    print("hello")
    # thing = SubRule(field1="string1",field2="string2",field3="string3")

    # print(thing)
    # print(thing.field1)
    # print(thing.field2)
    # print(thing.field3)
