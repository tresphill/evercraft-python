from src.character import character

class Rogue(Character):
    def __init__(self, name, align):
        Character.__init__(self, name, align)
        self.armor_class = 8
        self.hit_point = 7
        self.experience_points = 1
        self.level_of = 0
        self.abilities = {
            'Strength': 8,
            'Dexterity': 20,
            'Constitution': 10,
            'Wisdom': 10,
            'Intelligence': 10,
            'Charisma': 25
        }