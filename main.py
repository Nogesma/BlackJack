import init
import game

# Begins by initialising the players and the deck depending on the number of players
print()  # Empty prints are used for nicer display on the command line
numberOfPlayers = int(input("Enter the number of players: "))
print()

# Initialise players
Players = init.create_players(numberOfPlayers)
Dealer = init.Dealer()  # Initialise Dealer
# Create the deck of card
deck = init.create_deck(numberOfPlayers)
print()


gameIsOn = True  # Used to check if the game has ended

while gameIsOn:
    game.complete_game(Players, Dealer, deck)  # Start the game

    # Uses a deep copy of Players because the length of Players might change during the loop
    copyPlayers = Players[:]

    for player in copyPlayers:
        # If the player has under 2$, he can't bet anymore, he has lost
        if player.money < 2:
            print("{} has been eliminated")
            Players.remove(player)  # Remove the player from the game
        elif input("Do you wish to continue {} (y/n)?".format(player.name)) == "n":
            Players.remove(player)

    # If all the players stopped participating, the game finishes
    gameIsOn = len(Players) != 0

    # Reset the deck if it's less than half it's original size.
    # harder to count cards efficiently
    if len(deck) < 26 * numberOfPlayers:
        deck = init.create_deck(numberOfPlayers)
