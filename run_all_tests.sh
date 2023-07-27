#!/bin/bash

#
# run all tests
#

for x in ./tests/test*.py
do
    ${x}
done