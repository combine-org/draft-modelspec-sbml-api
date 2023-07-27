#!/usr/bin/env python3

'''
building up an SBML like example from a simple starting point
'''

import modelspec
from modelspec import field, instance_of, optional
from modelspec.base_types import Base
from typing import List

import re

def valid_sid(instance, attribute, value):
    if not re.fullmatch('[_A-Za-z][_A-Za-z0-9]*',value):
        raise ValueError("an SId must match the regular expression: [_A-Za-z][_A-Za-z0-9]*")

@modelspec.define
class SBase(Base):
    id: str = field(default=None,validator=optional([instance_of(str),valid_sid]))

@modelspec.define
class SBML(SBase):
    level:   str = field(default="3",validator=instance_of(str))
    version: str = field(default="2",validator=instance_of(str))

if __name__ == "__main__":
    import json
    import yaml

    path = "tests/untracked/test1"

    sbml_doc = SBML(id="sbml_example")


    sbml_doc.to_json_file(f"{path}.json")
    sbml_doc.to_yaml_file(f"{path}.yaml")
    sbml_doc.to_bson_file(f"{path}.bson")
    #sbml_doc.to_xml_file(f"{path}.xml")

    print(sbml_doc.id)


    open(f"{path}.docs.md", "w").write(sbml_doc.generate_documentation(format="markdown"))

    open(f"{path}.docs.rst", "w").write(sbml_doc.generate_documentation(format="rst"))

    doc_dict = sbml_doc.generate_documentation(format="dict")
    open(f"{path}.docs.json", "w").write(json.dumps(doc_dict, indent=4))
    open(f"{path}.docs.yaml", "w").write(yaml.dump(doc_dict, indent=4, sort_keys=False))
