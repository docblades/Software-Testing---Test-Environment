#!/usr/bin/python
import testenv_blackbox_decisiontable as testenv

# Example
# None is the same as a dash in the decision table

test_cases = [
    # (inc, dep, {action 1: [values True, False, or None], action 2: [values]})
    (1, 1,
     {1: [True, False, False, False, False, False],
      2: [True, False, False, False]}
     ),
    (20001, 1,
     {1: [False, True, False, False, False, False],
      2: [True, False, False, False]}
     ),
    (30001, 1,
     {1: [False, False, True, False, False, False],
      2: [True, False, False, False]}
     ),
    (40001, 1,
     {1: [False, False, False, True, False, False],
      2: [True, False, False, False]}
     ),
    (50001, 1,
     {1: [False, False, False, False, True, False],
      2: [True, False, False, False]}
     ),
    (90001, 1,
     {1: [False, False, False, False, False, True],
      2: [True, False, False, False]}
     ),
    (1, 2,  
     {1: [True, False, False, False, False, False],
      2: [False, True, False, False]}
     ),
    (20001, 2,
     {1: [False, True, False, False, False, False],
      2: [False, True, False, False]}
     ),
    (30001, 2,
     {1: [False, False, True, False, False, False],
      2: [False, True, False, False]}
     ),
    (40001, 2,
     {1: [False, False, False, True, False, False],
      2: [False, True, False, False]}
     ),
    (50001, 2,
     {1: [False, False, False, False, True, False],
      2: [False, True, False, False]}
     ),
    (90001, 2,
     {1: [False, False, False, False, False, True],
      2: [False, True, False, False]}
     ),
    (1, 4,
     {1: [True, False, False, False, False, False],
      2: [False, False, True, False]}
     ),
    (20001, 4,
     {1: [False, True, False, False, False, False],
      2: [False, False, True, False]}
     ),
    (30001, 4,
     {1: [False, False, True, False, False, False],
      2: [False, False, True, False]}
     ),
    (40001, 4,
     {1: [False, False, False, True, False, False],
      2: [False, False, True, False]}
     ),
    (50001, 4,
     {1: [False, False, False, False, True, False],
      2: [False, False, True, False]}
     ),
    (90001, 4,
     {1: [False, False, False, False, False, True],
      2: [False, False, True, False]}
     ),
    (1, 0,
     {1: [True, False, False, False, False, False],
      2: [False, False, False, True]}
     ),
    (20001, 0,
     {1: [False, True, False, False, False, False],
      2: [False, False, False, True]}
     ),
    (30001, 0,
     {1: [False, False, True, False, False, False],
      2: [False, False, False, True]}
     ),
    (40001, 0,
     {1: [False, False, False, True, False, False],
      2: [False, False, False, True]}
     ),
    (50001, 0,
     {1: [False, False, False, False, True, False],
      2: [False, False, False, True]}
     ),
    (90001, 0,
     {1: [False, False, False, False, False, True],
      2: [False, False, False, True]}
     )
    ]

testenv.do_test(test_cases)
