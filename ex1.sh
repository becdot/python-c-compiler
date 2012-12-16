#!/bin/sh
# Produce test outputs for ex1.py, given inputs in ex1.test-input;
# then make sure they're the same as expected.
# This is our top-level test script.

python ex1.py >ex1.c &&
gcc -o ex1 ex1.c &&
./ex1 <ex1.test-input >ex1.test-output
diff -u ex1.expected-output ex1.test-output
