# tests/test_fonctions_nulles.py
from chartoolbox.fonctions_nulles import salut

def test_fonctions_nulles():
    assert salut() == 'salut'
