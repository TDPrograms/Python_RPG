from rpg.character import Character


print("Hello World!")

player1 = Character()
player1.load_from_json("/character/luna.json")
player1.charisma = 14
player1.strength = 18

print(player1.name)
print(player1.charisma)
