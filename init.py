import numpy as np


class Player:
    def __init__(self):  # Initialise the class for a player
        # Default values :
        self.name = input("Enter the name of the player: ")  # Name of the player
        self.cards = []  # List of the cards of the player
        # Score of the player, a list is used for the case when the player has an ace
        self.score = [0, 0]
        self.hand = "Hard"  # Type of hand
        self.wins = 0  # Wins of player
        self.bet = 0  # Bet of the player
        self.money = 100  # Initial money of the player
        self.insurance = False  # Used to know if the player takes insurance


class Dealer:
    def __init__(self):
        self.name = "Dealer"
        self.cards = []
        self.score = [0, 0]
        self.hand = "Hard"


def create_deck(n):  # Create a deck of cards composed of n decks of 52 cards
    values = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "Ten",
        "Jack",
        "Queen",
        "King",
    ]
    types = ["Clubs", "Diamonds", "Hearts", "Spikes"]
    deck = [v + " of " + t for _ in range(n) for t in types for v in values]

    np.random.shuffle(deck)  # Shuffles the deck

    return deck


def create_players(n):  # Create n players
    return [Player() for _ in range(n)]
