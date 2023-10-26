import pytest
from src.character import Character
from src.dice import Dice
from src.AttackUtility import AttackUtility
from src.AttackStatus import AttackStatus

def test_run_iteration1():
    # create character obj
    char = Character('Bob Dos', "Good")
    # set the name in the function
    assert char.name is "Bob Dos"

def test_character_align():
    char = Character('Bob Dos','Good')
    assert char.align is 'Good'

def test_character_has_armor():
    # create character
    char = Character('Bob Dos', 'Good')
    # create dice object roll
    dice = Dice(10)
    # compare dice roll against char armor
    assert char.armor_class == 10

def test_character_hit():
    # create character
    char = Character('Bob Dos', 'Good')
    # set hit point to 5
    assert char.hit_point == 5

def test_combatant_can_attack():
    dice = Dice(20)
    assert dice.roll == 20

def test_combatant_successful_attack():
    opponent = Character("Opponent", "Good")
    dice = Dice(10)
    attack_value = dice.roll
    au = AttackUtility
    attack_status = au.eval_attack(opponent, attack_value)
    assert attack_status == AttackStatus.HIT

def test_combatant_critical_attack():
    opponent = Character("Opponent", "Good")
    dice = Dice(20)
    attack_value = dice.roll
    au = AttackUtility
    attack_status = au.eval_attack(opponent, attack_value)
    assert attack_status == AttackStatus.CRITICAL

def test_combatant_unsuccessful_attack():
    opponent = Character("Opponent", "Good")
    dice = Dice(9)
    attack_value = dice.roll
    au = AttackUtility
    attack_status = au.eval_attack(opponent, attack_value)
    assert attack_status == AttackStatus.MISS