#!/usr/bin/env python3

'''
test of the base class mechanism in modelspec
'''

import modelspec
from modelspec import field, instance_of, optional
from modelspec.base_types import Base
from typing import List

@modelspec.define
class SBase(Base):
    id:      str = field(default=None,validator=optional(instance_of(str)))
    name:    str = field(default=None,validator=optional(instance_of(str)))
    metaid:  str = field(default=None,validator=optional(instance_of(str)))
    sboTerm: str = field(default=None,validator=optional(instance_of(str)))

    notes:      str = field(default=None,validator=optional(instance_of(str)))
    annotation: str = field(default=None,validator=optional(instance_of(str)))

@modelspec.define
class Rule(SBase):

    math: str = field(default=None,validator=optional(instance_of(str)))

@modelspec.define
class SubRule(Rule):

    #variable: str = field(validator=instance_of(str))                        #error
    #variable: str = field(default=None,validator=instance_of(str))           #ok
    #variable: str = field(validator=optional(instance_of(str)))              #error
    #variable: str = field(default=None,validator=optional(instance_of(str))) #ok

if __name__ == "__main__":
    print("hello")
    # thing = SubRule(field1="string1",field2="string2",field3="string3")

    # print(thing)
    # print(thing.field1)
    # print(thing.field2)
    # print(thing.field3)
