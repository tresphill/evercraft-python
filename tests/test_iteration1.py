import pytest
from src.character import Character
from src.dice import Dice
from src.AttackUtility import AttackUtility
from src.AttackStatus import AttackStatus

# create character
def test_run_iteration1():
    # create character obj
    char = Character('Bob Dos', "Good")
    # set the name in the function
    assert char.name is "Bob Dos"

# character alignment 
def test_character_align():
    char = Character('Bob Dos','Good')
    assert char.align is 'Good'

# character armor
def test_character_has_armor():
    # create character
    char = Character('Bob Dos', 'Good')
    # create dice object roll
    dice = Dice(10)
    # compare dice roll against char armor
    assert char.armor_class == 10

# character hit points
def test_character_hit():
    # create character
    char = Character('Bob Dos', 'Good')
    # set hit point to 5
    assert char.hit_point == 5

# character can attack
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

# character can be damaged
# def test_can_be_damaged():
#     opponent = Character("Bob Not Dos", "Bad")
#     health = opponent.hit_point
#     opponent.char_damaged()
#     assert opponent.hit_point == 4
#     # if attack successful, hit 1 point
#     # if dice roll 20, hit 2 points
#     # when health 0, player is dead
    

# character can gain exp
def test_attack_gain_experience():
    character = Character("Bob Dos", "Good")
    initial_xp = character.experience_points

    character.attack("Opponent")
    assert character.experience_points == initial_xp + 10
  

# character can level up
def test_level_up():
    character = Character("Bob Dos", "Good")
    character.experience_points = 100
    initial_level = character.level_of
    
    character.level_up()
    assert character.level_of == initial_level + 1 


# def test_char_stat():
    