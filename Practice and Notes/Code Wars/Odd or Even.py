class RPS():
    def __init__(self):
        self.p1 = raw_input("Enter name P1: ")
        self.p2 = raw_input("Enter name P2: ")

    def play(self):
        self.choose()
    
    def choose(self):    
        self.p1_choice = raw_input("%s, select your move: " % self.p1).lower()
        self.p2_choice = raw_input("%s, select your move: " % self.p2).lower()
        self.compare(self.p1_choice, self.p2_choice)
        
    def compare(self, a, b):
        if a and b not in ["rock", "paper", "scissors"]:
            print "You did not enter a valid option."
            self.choose()
        if a == b:
            print "Draw! Go again..."
            self.choose()
        if (a == "rock" and b == "scissors") or \
           (a == "scissors" and b == "paper") or \
           (a == "paper" and b == "rock"):
           print "%s wins!" % self.p1
           return
        else:
            print "%s wins!" % self.p2
            return
                        
game1 = RPS()
game1.play()