#!/usr/bin/python

def calc_tax(inc, dep):
    bracket = 0
    if (0 < inc <= 20000):
        bracket = 1
    elif (20000 < inc <= 30000):
        bracket = 2
    elif (30000 < inc <= 40000):
        bracket = 3
    elif (40000 < inc <= 50000):
        bracket = 4
    elif (50000 < inc <= 90000):
        bracket = 5
    else:
        bracket = 6

    def switch(x):
        if x == 1:
            tax = inc * .04
        elif x == 2:
            tax = inc * .05
        elif x == 3:
            tax = inc * .06
        elif x == 4:
            tax = inc * .07
        elif x == 5:
            tax = inc * .10
        elif x == 6:
            tax = inc * .13
        else:
            print "something is wrong with the income bracket computation"
        return tax

    tax = switch(bracket)

    if (dep == 1):
        tax = tax - (.1 * tax)
    elif (2 <= dep <= 3):
        tax = tax - (.25 * tax)
    elif (3 < dep):
        tax = tax - (.4 * tax)
    else:
        tax = tax

    print "income = {0} dependent = {1} tax = {2}".format(inc, dep, tax)

    return (inc, dep, tax)
        
def is_correct(test_input, expected_output):
    actual_out = calc_tax(test_input[0], test_input[1])
    return actual_out == (test_input[0], test_input[1], expected_output)

def do_test(test_cases):
    failures = []
    for test_case in test_cases:
        test_in = test_case[0]
        test_out = test_case[1]
        if is_correct(test_in, test_out):
            print "*"
            continue
        else:
            print '-'
            failures.append((test_in, test_out, calc_tax(test_in[0], test_in[1])))

    for fail in failures:
        print "FAIL: input: ", fail[0], ", expected output: ", (fail[0][0], fail[0][1], fail[1]), ", actual output: ", fail[2]

    failnum = len(failures)
    testnum = len(test_cases)

    print "{0} of {1} test cases passed ({2:.1%})".format(testnum, testnum - failnum, float((testnum - failnum)) / testnum)
    

if __name__ == "__main__":
    print calc_tax(20000, 1)

    test_cases = [((20000, 1), 720.0),
                  ((30000, 0), 500.0)]
    do_test(test_cases)
