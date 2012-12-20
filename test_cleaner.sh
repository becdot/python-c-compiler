#!/bin/bash

# Removes generated test files
# <test>, <test>.c, <test>.test-input, <test>.test-output, <test>.expected-output


# bits
for test in ex1 ex2 ex3 ex4 mux dmux
do
if [ -e $test ]
    then
        rm $test $test.expected-output $test."test-input" $test."test-output" $test.c
fi
done
# bytes
for test in byte_and
do
if [ -e $test ]
    then
        rm $test $test.expected-output $test."test-input" $test."test-output" $test.c
fi
done