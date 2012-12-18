# Loops over all tests in test_bits.py and calls ex.sh on each.
# Top-level test script

#!/bin/bash
for test in ex1 ex2 ex3 ex4 mux dmux
do
./ex_test_bits.sh $test
done