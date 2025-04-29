from base_file import a,b, add_two_numbers, subtract_two_numbers, multiply_two_numbers, divide_two_numbers


print(a,b, add_two_numbers(a,b), subtract_two_numbers(a,b), 
      multiply_two_numbers(a,b), divide_two_numbers(a,b))

def test_a_functionality():

	assert add_two_numbers(2, 3) == 5, "Addition failed!"  # assert checks if the expression is True, if not it raises an AssertionError
	# assert checks if the expression is True, if not it raises an AssertionError


def test_b_functionality():

	assert subtract_two_numbers(5, 3) == 2, "Subtraction failed!"  # assert checks if the expression is True, if not it raises an AssertionError


def test_multiply_two_numbers():

	assert multiply_two_numbers(2, 3) == 6.0, "Multiplication failed!"  # assert checks if the expression is True, if not it raises an AssertionError