from AttackUtility import AttackUtility
from Ability import modify
from enum import Enum

class Character():
        abilities = []

    def __init__(self, name, align):
        self.name = name 
        self.align = align
        self.armor_class = 10
        self.hit_point = 5
        self.experience_points = 1
        self.level_of = 0
        self.create_ability()
    
    def attack(self, enemy):
        self.experience_points += 10

    def level_up(self):
        if self.experience_points == 100:
            self.level_of += 1 

    def set_abilities(self, ability, score):
        if ability in self.abilities and 1 <= score <= 20:
            self.abilities[ability] = score
    
    def char_damaged(self, enemy):
        eval_attack = AttackUtility
        if eval_attack == True :
            self.hit_point -= 1


    