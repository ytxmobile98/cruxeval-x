from typing import List, Dict, Tuple

def f(countries: Dict[None, None]) -> Dict[None, None]:
    """"""
    ### Canonical solution below ###
    language_country = dict()
    for (country, language) in countries.items():
        if language not in language_country:
            language_country[language] = []
        language_country[language].append(country)
    return language_country

### Unit tests below ###
def check(candidate):
    assert candidate({}) == {}

def test_check():
    check(f)

