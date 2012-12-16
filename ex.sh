#!/bin/sh
# Produce test outputs for ex1.py, given inputs in ex1.test-input;
# then make sure they're the same as expected.
# This is our top-level test script.

python $1.py >$1.c &&
gcc -o $1 $1.c &&
./$1 <$1.test-input >$1.test-output
diff -u $1.expected-output $1.test-output
