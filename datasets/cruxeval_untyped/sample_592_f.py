def f(numbers):
    """"""
    ### Canonical solution below ###
    new_numbers = []
    for i, _ in enumerate(numbers):
        new_numbers.append(numbers[len(numbers)-1-i])
    return new_numbers

def check(candidate):
    assert candidate([11, 3]) == [3, 11]

def test_check():
	check(f)