import init
import game
import copy

# Begins by initialising the players and the deck depending on the number of players
print()  # Empty prints are used for nicer display on the command line
numberOfPlayers = int(input('Enter the number of players: '))
print()

Players = init.create_players(numberOfPlayers)  # Call the function to initialise the players
Dealer = init.Dealer()  # Initialise the Dealer
deck = init.create_deck(numberOfPlayers)  # Create the deck of card depending on the number of players
print()


gameIsOn = True  # Used to check if the game has ended

while gameIsOn:

    game.complete_game(Players, Dealer, deck)  # Start the game

    # Uses a deep copy of Players because the length of Players might change during the loop
    copyPlayers = copy.copy(Players)

    for player in copyPlayers:

        if player.money < 2:  # If the player has under 2$, he can't bet anymore, he has lost

            print('{} has been eliminated')
            Players.remove(player)  # Remove the player from the game

        if input('Do you wish to continue {} (y/n)?'.format(player.name)) == 'n':

            Players.remove(player)

    if len(Players) == 0:  # If all the players stopped participating, the game finishes
        gameIsOn = False
