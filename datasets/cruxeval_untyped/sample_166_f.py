def f(graph):
    """"""
    ### Canonical solution below ###
    new_graph = {}
    for key, value in graph.items():
        new_graph[key] = {}
        for subkey in value:
            new_graph[key][subkey] = ''
    return new_graph

def check(candidate):
    assert candidate({}) == {}

def test_check():
	check(f)