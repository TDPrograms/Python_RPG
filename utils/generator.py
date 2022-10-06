import random

from rpg.character import Character

class Generator():
    def __init__(self):
        pass

    def character(self):
        char = Character()
        char.hit_p_max = 6
        char.intel = random.randint(3,19)
        char.race = random.choice("Human", "Dark Elf", "Dwarf", "Barbarian", "Druid")
        return char