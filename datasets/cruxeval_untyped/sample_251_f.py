def f(messages):
    """"""
    ### Canonical solution below ###
    phone_code = "+353"
    result = []
    for message in messages:
        message.extend(phone_code)
        result.append(";".join(message))
    return ". ".join(result)

def check(candidate):
    assert candidate([['Marie','Nelson','Oscar']]) == 'Marie;Nelson;Oscar;+;3;5;3'

def test_check():
	check(f)