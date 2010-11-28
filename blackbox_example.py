#!/usr/bin/python

import mainstuff

#test cases = [((inc, dep), expected_output), ((inc2, dep2), expect_output2), ...]
#expected_output is the tax value returned from the program

test_cases = [
    ((0,1), 0),
    ((20000, 2), 600)
    ]

mainstuff.do_test(test_cases)
