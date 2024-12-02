def f(plot, delin):
    """"""
    ### Canonical solution below ###
    if delin in plot:
        split = plot.index(delin)
        first = plot[:split]
        second = plot[split + 1:]
        return first + second
    else:
        return plot

def check(candidate):
    assert candidate([1, 2, 3, 4], 3) == [1, 2, 4]

def test_check():
	check(f)