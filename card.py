import sys
import pyCardDeck
from typing import List
from pyCardDeck.cards import PokerCard

class Player:
    def __init__(self, name: str): 
        self.hand = [] 
        self.name = name
    def __str__(self): 
        return self.name

class jackGame:
    def __init__(self, players: List[Player]): 
        self.deck = pyCardDeck.Deck()
        self.deck.load_standard_deck() 
        self.players = players
        self.scores = {} 
        print("Created a game with {} players.".format(len(self.players)))

    def blackjack(self):
        print("Setting up...") 
        print("Shuffling...") 
        self.deck.shuffle() 
        print("All shuffled!") 
        print("Dealing...") 
        self.deal() 
        print("\nLet's play!") 
        for player in self.players: 
            print("{}'s turn...".format(player.name)) 
            print("playerrrrrr",player.hand)
            self.play(player) 
        else: 
            print("That's the last turn. Determining the winner...") 
            self.find_winner()

    def deal(self): 
        for _ in range(2):
            for p in self.players: 
                newcard = self.deck.draw()
                while(newcard=="Ten of Clubs" or newcard=="Ten of Diamonds" or newcard=="Ten of Spades" or newcard=="Ten of Hearts"):
                    newcard = self.deck.draw()
                p.hand.append(newcard)
                print(p.hand)
                print("Dealt {} the {}.".format(p.name, str(newcard)))

    def find_winner(self):
        winners = [] 
        try: 
            win_score = max(self.scores.values()) 
            for key in self.scores.keys(): 
                if self.scores[key] == win_score: 
                    winners.append(key) 
                else: 
                    pass 
            winstring = " & ".join(winners) 
            print("And the winner is...{}!".format(winstring))
        except ValueError: 
            print("Whoops! Everybody lost!")

    def hit(self, player):
        newcard = self.deck.draw() 
        while(newcard=="Ten of Clubs" or newcard=="Ten of Diamonds" or newcard=="Ten of Spades" or newcard=="Ten of Hearts"):
            newcard = self.deck.draw()
        player.hand.append(newcard) 
        print(" Drew the {}.".format(str(newcard)))

    def play(self, player):
        while True: 

            points = sum_hand(player.hand)
            if points < 17: 
                print(" Hit.")
                self.hit(player) 
            elif points == 21: 
                print(" {} wins!".format(player.name)) 
                sys.exit(0) # End if someone wins 
            elif points > 21: 
                print(" Bust!") 
                break 
            else: # Stand if between 17 and 20 (inclusive) 
                print(" Standing at {} points.".format(str(points))) 
                self.scores[player.name] = points 
                break

def sum_hand(hand: list):
    vals = [card.rank for card in hand]
    intvals = [] 
    while len(vals) > 0: 
        value = vals.pop()
        try: 
            intvals.append(int(value))
        except ValueError: 
            if value in ['K', 'Q', 'J']: 
                intvals.append(10) 
            elif value == 'A': 
                intvals.append(1) # Keep it simple for the sake of example 
    if intvals == [1, 10] or intvals == [10, 1]: 
        print(" Blackjack!") 
        return(21) 
    else: 
        points = sum(intvals) 
        print(" Current score: {}".format(str(points))) 
        return(points)

if name == "main": 
    game = jackGame([Player("Kit"), Player("Anya"), Player("Iris"), Player("Simon")]) 
    game.blackjack()

