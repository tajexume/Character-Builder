import datetime

import pytest
from ..character_builder import FakeCharacter


def test_Build_Character():
    test_character = FakeCharacter(gender="M")
    assert test_character.characterID == -1
    assert test_character.gender == "M"
    assert test_character.race == "AA"
    assert test_character.height == 68
    assert test_character.weight == 180
    assert test_character.bio == ""
    assert test_character.dob == datetime.date.today()
    assert test_character.creator == "Unkown"
