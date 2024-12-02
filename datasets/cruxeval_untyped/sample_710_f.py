def f(playlist, liker_name, song_index):
    """"""
    ### Canonical solution below ###
    playlist[liker_name] = playlist.get(liker_name, [])
    playlist[liker_name].append(song_index)
    return playlist

def check(candidate):
    assert candidate({'aki': ['1', '5']}, 'aki', '2') == {'aki': ['1', '5', '2']}

def test_check():
	check(f)