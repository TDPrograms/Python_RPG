from rpg.character import Character
from rpg.weapon import Weapon
from rpg.armor import Armor
from utils.generator import Generator

print("Hello World!")

dagger = Weapon()
print(dagger.name)
dagger.load("weapons/daggers.json")
print(dagger.name)

chainmail = Armor()
print(chainmail.name)
chainmail.load("armor/chainmail.json")
print(chainmail.name)

luna = Character()
luna.load_from_json("characters/luna.json")
print(luna.name, luna.charisma)

char = Generator()
new_char = char.character
print(char.race, char.intel)