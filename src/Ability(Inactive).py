from enum import Enum

class Ability(Enum):
        Strength = 1
        Dexterity = 2
        Constitution = 3
        Wisdom = 4
        Intelligence = 5
        Charisma = 6

class AbilityScore:
        def __init__(self, ability):
                self.ability = ability
                self.score = 10
                self.mod = 0

        def get_score(self):
                return self.score

        def get_mod(self):
                return self.mod
        
        def set_score(self,num):
                self.score = num
                self.mod = self.score_to_mod(num)

        score = property(get_score, set_score)
        mod = property(get_mod)
                

        def modify(self, score):
            mods = {
            20: 5,
            19: 4,
            18: 4,
            17: 3,
            16: 3,
            15: 2,
            14: 2,
            13: 1,
            12: 1,
            11: 0,
            10: 0,
            9: -1,
            8: -1,
            7: -2,
            6: -2,
            5: -3,
            4: -3,
            3: -4,
            2: -4,
            1: -5
        }
            return mods.get(score)