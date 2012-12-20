# Produce test outputs for <test_name> in test_*.py
# Given inputs in <test_name>.test-input, diffs <test_name>.test-output with <test_name>.expected-output
# This is run by test_runner.sh <arg1> <arg2>, where arg1 = what is being tested (e.g. bits) and arg2 = <test_name>

#!/bin/sh

if [ $1 = "bits" ]
then
    python test_bits.py $2>$2.c &&
    gcc -o $2 $2.c &&
    ./$2 <$2.test-input >$2.test-output
    diff -u $2.expected-output $2.test-output
elif [ $1 = "bytes" ]
then
    python test_bytes.py $2>$2.c &&
    gcc -o $2 $2.c &&
    ./$2 <$2.test-input >$2.test-output
    diff -u $2.expected-output $2.test-output
fi
