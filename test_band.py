import pytest

from band import Bands, Musician, Singer, Guitarist, Drummer

def test_member_one():
    test_drummer = Drummer('Ashlyn')
    assert isinstance(test_drummer, Drummer)

def test_member_two():
    test_singer = Singer('Kathy')
    assert isinstance(test_singer, Singer)

def test_member_three():
    test_guitarist = Guitarist('Sean')
    assert isinstance(test_guitarist, Guitarist)