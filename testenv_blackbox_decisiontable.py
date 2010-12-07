#!/usr/bin/python

def calc_tax(inc, dep):
    bracket = 0
    actions = {1: [False, False, False, False, False, False, False],
               2: [False, False, False, False]}
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
            actions[1][0] = True
        elif x == 2:
            tax = inc * .05
            actions[1][1] = True
        elif x == 3:
            tax = inc * .06
            actions[1][2] = True
        elif x == 4:
            tax = inc * .07
            actions[1][3] = True
        elif x == 5:
            tax = inc * .10
            actions[1][4] = True
        elif x == 6:
            tax = inc * .13
            actions[1][5] = True
        else:
            print "something is wrong with the income bracket computation"
            actions[1][6] = True
        return tax

    tax = switch(bracket)

    if (dep == 1):
        tax = tax - (.1 * tax)
        actions[2][0] = True
    elif (2 <= dep <= 3):
        tax = tax - (.25 * tax)
        actions[2][1] = True
    elif (3 < dep):
        tax = tax - (.4 * tax)
        actions[2][2] = True
    else:
        tax = tax
        actions[2][3] = True

    print "income = {0} dependent = {1} tax = {2}".format(inc, dep, tax)

    return (inc, dep, actions)
        
def is_correct(test_input, expected_actions):
    actual_out = calc_tax(test_input[0], test_input[1])
    actual_actions = actual_out[2]
    for i in range(0, 6):
        if expected_actions[1][i] == None:
            continue
        if expected_actions[1][i] != actual_actions[1][i]:
            return False
    for i in range(0, 4):
        if expected_actions[2][i] == None:
            continue
        if expected_actions[2][i] != actual_actions[2][i]:
            return False
    return True

def do_test(test_cases):
    failures = []
    for test_case in test_cases:
        test_in = test_case
        expected_actions = test_case[2]
        if is_correct(test_in, expected_actions):
            print "PASS"
            continue
        else:
            print 'FAIL'
            failures.append((test_in, expected_actions, calc_tax(test_in[0], test_in[1])))

    for fail in failures:
        print "FAIL: input: ", (fail[0][0], fail[0][1])
        print "expected actions: ", fail[1]
        print "actual actions: ", fail[2][2]

    failnum = len(failures)
    testnum = len(test_cases)

    print "{1} of {0} test cases passed ({2:.1%})".format(testnum, testnum - failnum, float((testnum - failnum)) / testnum)
    

if __name__ == "__main__":
    print calc_tax(20000, 1)

    test_cases = [((20000, 1), 720.0),
                  ((30000, 0), 500.0)]
    do_test(test_cases)
