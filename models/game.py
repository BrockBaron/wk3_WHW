class Game():
    def __init__(self, p1, p2):
        self.p1= p1
        self.p2 = p2

    def play_rps(self):
        if self.p1.player_choice == self.p2.player_choice:
            return None
            
        elif self.p1.player_choice == "rock":
            if self.p2.player_choice == "scissors":
                return self.p1
            else:
                return self.p2
                
        elif self.p1.player_choice == "paper":
            if self.p2.player_choice == "rock":
                return self.p1
            else:
                return self.p2
                
        elif self.p1.player_choice == "scissors":
            if self.p2.player_choice == "paper":
                return self.p1
            else:
                return self.p2