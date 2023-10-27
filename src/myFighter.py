from src.character import Character

class Fighter(Character):
    def __init__(self, name, align):
        Character.__init__(self, name, align)
        self.armor_class = 20
        self.hit_point = 10
        self.experience_points = 1
        self.level_of = 0
        self.abilities = {
            'Strength': 15,
            'Dexterity': 10,
            'Constitution': 20,
            'Wisdom': 10,
            'Intelligence': 2,
            'Charisma': 10
        }
