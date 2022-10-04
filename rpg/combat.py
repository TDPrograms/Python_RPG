from operator import truediv


class Combat():
    def __init__(self):
        #no idea if im doing this right but im trying!!!
        self.player_characters = []
        self.npc = []
        self.interactive_mode = False
        self.party_xp = 0
        self.party_success = False
        self.ordered_combatants = []
        self.player_ply_function = ""
        self.endgame_function = ""
	#are_all_characters_dead
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