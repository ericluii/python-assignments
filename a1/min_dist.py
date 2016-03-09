# Create the python function min_dist that consumes six floats
#                 x1, y1, x2, y2, x3, y3
# Which corresponds to the x, y coordinates of three friends'
# houses. So House1 is located at (x1, y1), House2 is located
# at (x2, y2), and House3 is located at (x3, y3).
#
# The function should take in these coordinates and output
# which house that all the friends should meet at. The
# house that they should meet at is decided by the house
# that is closest to all three houses(or the middle of all three)
#
# Another way to look at it, is the total distance that all three
# friends have to travel is minimized.
#
# The calculation you should use for calculating the distance is
# called Euclidean distance. Google and read up on how to calculate it
# if you don't know what it is :3

def min_dist(x1, y1, x2, y2, x3, y3):
    # TODO: Put your code here
    return "House19930801"

# The below will do some simple tests
# to see if you're doing it correctly
# you can read through to understand what it is doing
# but you don't need to change any code below (:
def check_answer(x1, y1, x2, y2, x3, y3, expected_answer):
    answer = min_dist(x1, y1, x2, y2, x3, y3);
    color = "\033[92m" if answer == expected_answer else "\033[91m"
    print "\tInput: House1({0}, {1}), House2({2}, {3}), House3({4}, {5})".format(x1, y1, x2, y2, x3, y3)
    print "\tExpected Output: {0}".format(expected_answer)
    print color + "\tActual Output: {0}\033[0m\n".format(answer)

print "Test Results: \033[92mGreen\033[0m means you're correct, \033[91mRed\033[0m means try again."
check_answer(1, 1, 3, 6, 2, 2, "House3")
check_answer(0, 0, 2, 0, 1, 10, "House1")
