# Produce test outputs for ex[i].py, given inputs in ex[i].test-input;
# then make sure they're the same as expected.
# This should be run by test_runner.sh, which calls this script for all tests defined in test_bits.py

#!/bin/sh
python test_bytes.py $1>$1.c &&
gcc -o $1 $1.c &&
./$1 <$1.test-input >$1.test-output
diff -u $1.expected-output $1.test-output
