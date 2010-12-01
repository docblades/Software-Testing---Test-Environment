import decision_table_stuff as testenv

# Example
# None is the same as a dash in the decision table

test_cases = [
    # (inc, dep, {action 1: [values True, False, or None], action 2: [values]})
    (1,
     0,
     {1: [True, False, False, False, False, False],
      2: [False, False, False, True]}
     ),
    (20001,
     1,
     {1: [False, True, False, False, False, False],
      2: [True, False, False, False]}
     ),
    (30001,
     2,
     {1: [False, False, True, None, None, None],
      2: [False, True, None, None]}
     )
    ]

test_env.do_test(test_cases)
