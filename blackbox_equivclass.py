#!/usr/bin/python
import mainstuff
#test case = (income, dependents, expected tax to 16 decimals)

test_cases = [
    (0, 0, 0),
    (1, 1, 1.321354252453)
    ]

mainstuff.do_test(test_cases)
