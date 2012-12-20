# Loops over tests and calls test_getter.sh on each, which compiles and executes test.c
# Top-level test script

#!/bin/bash
if [ $1 = "bits" ]
then
    for test in ex1 ex2 ex3 ex4 mux dmux
    do
        ./test_getter.sh $1 $test
done
elif [ $1 = "bytes" ]
then
    for test in byte_and
    do
        ./test_getter.sh $1 $test
done
fi