import inc_dec    # The code to test

def test_increment():
    assert inc_dec.increment(3) == 4
# The above code is a simple test that checks if the increment function returns
# the expected value. It does this by first defining test_increment as a
# function, which then has the assertain that calls the increment function with
# the argument 3 and checks if the return value is 4.

# This test is designed to fail for demonstration purposes.
def test_decrement():
    assert inc_dec.decrement(3) == 2
# The above code is similiar to the code on line 3:4, but this time it checks if
# the decrement function returns the expected value.