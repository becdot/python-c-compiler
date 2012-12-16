#!/bin/sh
# Produce test outputs for ex1.py, given inputs in ex1.test-input;
# then make sure they're the same as expected.
# This is our top-level test script.

python ex2.py >ex2.c &&
gcc -o ex2 ex2.c &&
./ex2 <ex2.test-input >ex2.test-output
diff -u ex2.expected-output ex2.test-output
