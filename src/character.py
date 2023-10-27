from src.AttackUtility import AttackUtility
from src.Ability import AbilityScore
from enum import Enum

class Character():
    def __init__(self, name, align):
        self.name = name 
        self.align = align
        self.armor_class = 10
        self.hit_point = 5
        self.experience_points = 1
        self.level_of = 0
        #self.create_ability()
        self.abilities = {
            'Strength': 10,
            'Dexterity': 10,
            'Constitution': 10,
            'Wisdom': 10,
            'Intelligence': 10,
            'Charisma': 10
        }
    
    def attack(self, enemy):
        self.experience_points += 10

    def level_up(self):
        if self.experience_points == 100:
            self.level_of += 1 
        
    def set_ability_score(self, ability, score):
        if ability in self.abilities and 1 <= score <= 20:
            self.abilities[ability] = score

    def get_ability_modifier(self, ability):
        if ability in self.abilities:
            score = self.abilities[ability]
            if 1 <= score <= 20:
                modifiers = {
                    1: -5, 2: -4, 3: -4, 4: -3, 5: -3, 6: -2, 7: -2,
                    8: -1, 9: -1, 10: 0, 11: 0, 12: 1, 13: 1,
                    14: 2, 15: 2, 16: 3, 17: 3, 18: 4, 19: 4, 20: 5
                }
                return modifiers[score]
    
    def char_damaged(self, enemy):
        # if AttackUtility(enemy):
        self.hit_point -= 1


    