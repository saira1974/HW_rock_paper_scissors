import random
from models.player import *

class game:

    def __init__(self):
        self.win_lookup = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }
    
    def check_win(self, player1, player2):
        hand1 = player1.hand.lower()
        hand2 = player2.hand.lower()

        winner = None

        if self.win_lookup.get(hand1) == hand2:
            winner = player1
        elif self.win_lookup.get(hand2) == hand1:
            winner = player2
        return winner



