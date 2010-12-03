#!/usr/bin/python
import decision_table_stuff as testenv

# Example
# None is the same as a dash in the decision table

test_cases = [
    # (inc, dep, {action 1: [values True, False, or None], action 2: [values]})
    (1,  # TEST CASE 1 0 < inc <= 20000
     1,  # dep 1
     {1: [True, False, False, False, False, False, False],
      2: [True, False, False, False]}
     ),
    (20001, # TEST CASE 2 20000 < inc <= 30000
     1,  #dep 1
     {1: [False, True, False, False, False, False, False],
      2: [True, False, False, False]}
     ),
    (30001,  # TEST CASE 3 30000 < inc <= 40000
     1,    #dep 1
     {1: [False, False, True, False, False, False, False],
      2: [True, False, False, False]}
     ) 
    (40001, # TEST CASE 4  40000 < inc <= 50000
     1,
     {1: [False, False, False, True, False, False, False],
      2: [True, False, False, False]}
     )
    (50001, # Test case 5  50000 < inc <= 90000
     1,  #dep 1
     {1: [False, False, False, False, True, False, False],
      2: [True, False, False, False]}
     )
    (90001,  # Test case 6  90000 < inc
     1,   #dep 1
     {1: [False, False, False, False, False, False, True],
      2: [True, False, False, False]}
     )
    (0,  #Test Case 7    inc = 0
     1,  #dep = 1
     {1: [False, False, False, False, False, True, False],
      2: [True, False, False, False]}
     )
    (1,  # Test case 8  0 < inc <= 20000 
     2,  # dep = 2
     {1: [True, False, False, False, False, False, False],
      2: [False, True, False, False]}
     ),
    (20001, 
     2,
     {1: [False, True, False, False, False, False, False],
      2: [False, True, False, False]}
     ),
    (30001,
     2,
     {1: [False, False, True, False, False, False, False],
      2: [False, True, False, False]}
     )
    (40001,
     2,
     {1: [False, False, False, True, False, False, False],
      2: [False, True, False, False]}
     )
    (50001,
     2,
     {1: [False, False, False, False, True, False, False],
      2: [False, True, False, False]}
     )
    (90001,
     2,
     {1: [False, False, False, False, False, False, True],
      2: [False, True, False, False]}
     )
    (0,
     2,
     {1: [False, False, False, False, False, True, ],
      2: [False, True, False, False]}
     )
    (1, #Test Case 15    0 < inc <= 20000
     4, #dep =4
     {1: [True, False, False, False, False, False, False],
      2: [False, False, True, False]}
     ),
    (20001, 
     4,
     {1: [False, True, False, False, False, False, False],
      2: [False, False, True, False]}
     ),
    (30001,
     4,
     {1: [False, False, True, False, False, False, False],
      2: [False, False, True, False]}
     )
    (40001,
     4,
     {1: [False, False, False, True, False, False, False],
      2: [False, False, True, False]}
     )
    (50001,
     4,
     {1: [False, False, False, False, True, False, False],
      2: [False, False, True, False]}
     )
    (90001,
     4,
     {1: [False, False, False, False, False, False, True],
      2: [False, False, True, False]}
     )
    (0,
     4,
     {1: [False, False, False, False, False, True, False],
      2: [False, False, True, False]}
     )
    (1, #Test Case 22  0 < inc <= 20000
     0,  #dep = 0
     {1: [True, False, False, False, False, False, False],
      2: [False, False, False, True]}
     ),
    (20001, 
     0,
     {1: [False, True, False, False, False, False, False],
      2: [False, False, False, True]}
     ),
    (30001,
     0,
     {1: [False, False, True, False, False, False, False],
      2: [False, False, False, True]}
     )
    (40001,
     0,
     {1: [False, False, False, True, False, False, False],
      2: [False, False, False, True]}
     )
    (50001,
     0,
     {1: [False, False, False, False, True, False, False],
      2: [False, False, False, True]}
     )
    (90001,
     0,
     {1: [False, False, False, False, False, False, True],
      2: [False, False, False, True]}
     )
    (0,
     0,
     {1: [False, False, False, False, False, True, False],
      2: [False, False, False, True]}
     )
    ]

testenv.do_test(test_cases)
