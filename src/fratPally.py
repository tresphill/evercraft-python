from src.character import Character

class Paladin(Character):
    def __init__(self, name, align):
        Character.__init__(self, name, align)
        self.armor_class = 5
        self.hit_point = 5
        self.experience_points = 1
        self.level_of = 0
        self.abilities = {
            'Strength': 15,
            'Dexterity': 10,
            'Constitution': 20,
            'Wisdom': 2,
            'Intelligence': 4,
            'Charisma': 20
        }