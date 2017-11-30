"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Carson Meyer.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math as mt

def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_cosines()
    run_test_sum_square_roots()


def run_test_sum_cosines():
    """ Tests the   sum_cosines   function. """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function.
    #   It TESTS the  sum_cosines  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_cosines   function:')
    print('--------------------------------------------------')

    #Test1
    print('Test 1')
    expected1 = 1.1241554693209974
    answer1 = sum_cosines(3)
    print('expected =', expected1)
    print('answer =', answer1)
    if (expected1 == answer1):
        print('Sweet Sassy Molassy!')

    #Test2
    print('Test 2')
    expected2 = -0.5194806481430599
    answer2 = sum_cosines(5)
    print('expected =', expected2)
    print('answer =', answer2)
    if (expected2 == answer2):
        print('Sweet Sassy Molassy!')

    #Test3
    print('Test 3')
    expected3 = 1.478254078313837
    answer3 = sum_cosines(8)
    print('expected =', expected3)
    print('answer =', answer3)
    if (expected3 == answer3):
        print('Sweet Sassy Molassy!')

def sum_cosines(n):
    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the cosines of the integers
       0, 1, 2, 3, ... n, inclusive, for the given n.
    Side effects:   None.
    Example:
      If n is 3, this function returns
        cos(0) + cos(1) + cos(2) + cos(3)   which is about 0.13416.
    """
    cos_val = 0
    for k in range(n):
        cos_val = cos_val + mt.cos(k)

    return cos_val
    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_cosines  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------


def run_test_sum_square_roots():
    """ Tests the   sum_square_roots   function. """
    # ------------------------------------------------------------------
    # DONE: 4. Implement this function.
    #   It TESTS the  sum_square_roots  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_square_roots   function:')
    print('--------------------------------------------------')

    #Test1
    print('Test 1')
    expected1 = 15.811388300841898
    answer1 = sum_square_roots(5)
    print('expected =', expected1)
    print('answer =', answer1)
    if (expected1 == answer1):
        print('Sweet Sassy Molassy!')

    #Test2
    print('Test 2')
    expected2 = 20.784609690826525
    answer2 = sum_square_roots(6)
    print('expected =', expected2)
    print('answer =', answer2)
    if (expected2 == answer2):
        print('Sweet Sassy Molassy!')

    #Test3
    print('Test 3')
    expected3 = 32.0
    answer3 = sum_square_roots(8)
    print('expected =', expected3)
    print('answer =', answer3)
    if (expected3 == answer3):
        print('Sweet Sassy Molassy!')

def sum_square_roots(n):
    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the square roots of the integers
       2, 4, 6, 8, ... 2n    inclusive, for the given n.
           So if n is 7, the last term of the sum is
           the square root of 14 (not 7).
    Side effects:   None.
    Example:
      If n is 5, this function returns
         sqrt(2) + sqrt(4) + sqrt(6) + sqrt(8) + sqrt(10),
      which is about 11.854408.
    """
    total = 0
    for k in range(n):
        total = total + mt.sqrt(n * 2)

    return total

    # ------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_square_roots  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
