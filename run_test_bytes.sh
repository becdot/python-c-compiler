# Loops over all tests in test_bits.py and calls ex.sh on each.
# Top-level test script

#!/bin/bash
for test in byte_and
do
./ex.test_bytes.sh $test
done