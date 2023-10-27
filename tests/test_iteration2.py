from src.myFighter import Fighter
import pytest
from src.character import Character
from src.dice import Dice
from src.AttackUtility import AttackUtility
from src.AttackStatus import AttackStatus

def test_fighter_character():
    char = Fighter("Reece", "Bad")
    assert char.name is 'Reece'


def test_character_align():
    char = Fighter('Bob Dos','Good')
    assert char.align is 'Good'