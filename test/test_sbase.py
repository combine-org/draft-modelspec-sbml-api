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
    field1:      str = field(default="some value",validator=instance_of(str))

@modelspec.define
class Rule(SBase):
    field2:      str = field(default=None,validator=optional(instance_of(str)))

def test_sbase():
    rule = Rule()

    print(rule.field2)

if __name__ == "__main__":
    test_sbase()
