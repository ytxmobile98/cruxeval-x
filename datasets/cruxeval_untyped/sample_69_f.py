def f(student_marks, name):
    """"""
    ### Canonical solution below ###
    if name in student_marks:
        value = student_marks.pop(name)
        return value
    return 'Name unknown'

def check(candidate):
    assert candidate({'882afmfp': 56}, '6f53p') == 'Name unknown'

def test_check():
	check(f)