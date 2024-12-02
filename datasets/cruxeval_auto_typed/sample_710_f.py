from typing import List, Dict, Tuple

def f(playlist: Dict[str, List[str]], liker_name: str, song_index: str) -> Dict[str, List[str]]:
    """"""
    ### Canonical solution below ###
    playList[liker_name] = playlist.get(liker_name, [])
    playList[liker_name].append(song_index)
    return playlist

### Unit tests below ###
def check(candidate):
    assert candidate({'aki': ['1', '5']}, 'aki', '2') == {'aki': ['1', '5', '2']}

def test_check():
    check(f)

