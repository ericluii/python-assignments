# Create a python function sum_of_digits that consumes an integer x
# and produces the sum of its digits
#
# GOOD LUCK

def sum_of_digits(x):
    # TODO: Put your code here
    return "19930801"

# The below will do some simple tests
# to see if you're doing it correctly
# you can read through to understand what it is doing
# but you don't need to change any code below (:
def check_answer(x, expected_answer):
    answer = sum_of_digits(x);
    color = "\033[92m" if answer == expected_answer else "\033[91m"
    print "\tInput: {0}".format(x) 
    print "\tExpected Output: {0}".format(expected_answer)
    print color + "\tActual Output: " + answer + "\033[0m\n"

print "Test Results: \033[92mGreen\033[0m means you're correct, \033[91mRed\033[0m means try again."
check_answer(235, 10)
check_answer(-13, 4)
check_answer(100001, 2)
check_answer(42, 6)
