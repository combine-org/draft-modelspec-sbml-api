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
    #field1:      str = field(default=None,validator=optional(instance_of(str)))
    field1:      str = field(default=None,validator=instance_of(str))

@modelspec.define
class Rule(SBase):
    field2:      str = field(default=None,validator=optional(instance_of(str)))
    #field2:      str = field(default=None,validator=instance_of(str))

@modelspec.define
class SubRule(Rule):
    field3:      str = field(default=None,validator=optional(instance_of(str)))
    #field3:      str = field(default=None,validator=instance_of(str))

if __name__ == "__main__":
    thing = SubRule(field1="string1",field2="string2",field3="string3")

    print(thing)
    print(thing.field1)
    print(thing.field2)
    print(thing.field3)
