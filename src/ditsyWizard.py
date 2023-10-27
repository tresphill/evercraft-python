from src.character import Character

class Wizard(Character):
    def __init__(self, name, align):
        Character.__init__(self, name, align)
        self.armor_class = 5
        self.hit_point = 5
        self.experience_points = 1
        self.level_of = 0
        self.abilities = {
            'Strength': 8,
            'Dexterity': 7,
            'Constitution': 3,
            'Wisdom': 4,
            'Intelligence': 30,
            'Charisma': 7
        }