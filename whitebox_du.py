#!/usr/bin/python

import testenv_whitebox as testenv

test_cases = [
    (0, 1),
    (20000, 2),
    (30000, 4),
    (40000, 0),
    (50000, 1),
    (90000, 2),
    (90001, 4),
    ]

testenv.do_test(test_cases)
