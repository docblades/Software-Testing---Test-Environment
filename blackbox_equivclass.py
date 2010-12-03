#!/usr/bin/python
import mainstuff
#test case = (income, dependents, expected tax to 16 decimals)

##############################
# test_cases = [             #
#     (0, 0, 0),             #
#     (1, 1, 1.321354252453) #
#     ]                      #
##############################

test_cases = [
    ((95000, 0), 12350.0),
    ((95000, 1), 11115.0),
    ((95000, 2), 9262.50),
    ((95000, 4), 7410.0),
    ((70000, 0), 7000.0),
    ((70000, 1), 6300.0),
    ((70000, 2), 5250.0),
    ((70000, 4), 4200.0),
    ((45000, 0), 3150.0000000000005),
    ((45000, 1), 2835.0000000000005),
    ((45000, 2), 2362.5000000000005),
    ((45000, 4), 1890.0000000000002),
    ((35000, 0), 2100.0),
    ((35000, 1), 1890.0),
    ((35000, 2), 1575.0),
    ((35000, 4), 1260.0),
    ((25000, 0), 1250.0),
    ((25000, 1), 1125.0),
    ((25000, 2), 937.50),
    ((25000, 4), 750.00),
    ((12000, 0), 480.00),
    ((12000, 1), 432.00),
    ((12000, 2), 360.00),
    ((12000, 4), 288.00),
    # Expecting Failure Here
    ((-5000, 0), 0),
    ((-5000, 1), 0),
    ((-5000, 2), 0),
    ((-5000, 4), 0)
    ]

mainstuff.do_test(test_cases)
