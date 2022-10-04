from operator import truediv


class Combat():
    def __init__(self):
        #no idea if im doing this right but im trying!!!
        self.player_characters = "character.py"
        self.npc = "monster.py"
        self.interactive_mode = True
        self.party_xp = 0
        self.party_success = True
        self.ordered_combatants = 0
        self.player_ply_function = ""
        self.endgame_function = ""

    def characters_dead(self):
        pass

    def combat_over(self):
        pass
    
    def end_combat(self):
        pass

    def ply(self):
        pass
        
    def print_stats(self):
        pass
    
    def turn(self):
        pass

    def start(self):
        pass