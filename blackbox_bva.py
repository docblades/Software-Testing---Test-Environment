#!/usr/bin/python

import testenv_blackbox as testenv

test_cases = [
    ((-1, 0), 0), #expecting a failure here
    ((0, 1), 0),
    ((20000, 2), 600),
    ((20001, 3), 750.0375),
    ((30000, 4), 900),
    ((30001, 0), 1800.06),
    ((40000, 1), 2160),
    ((40001, 2), 2100.0525000000002),
    ((50000, 3), 2625.0000000000005),
    ((90000, 0), 9000),
    ((90001, 1), 10530.117)
    ]

testenv.do_test(test_cases)
