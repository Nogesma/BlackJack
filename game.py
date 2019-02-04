import time  # Module used to 'pause' the program, so the players have time to read the actions


def dealer(player):  # function to determine if the dealer hit or stand
    score(player)
    return max(player.score) < 17


def score(player):  # Calculates the score of the player

    player.score = [0, 0]
    number_of_aces = 0  # Count the number of aces

    for card in range(len(player.cards)):

        value = player.cards[card][0]  # Takes the first character of each of the player's cards

        if value.isdigit():  # Check if the card is 2-9

            # Adds the value of the card to each entry in the list
            player.score = [x + int(value) for x in player.score]

        elif value != 'A':  # Check if the card is an ace

            # Adds 10 to each entry in the list
            player.score = [x + 10 for x in player.score]

        else:  # The card must be an Ace

            number_of_aces += 1

    if number_of_aces > 0:
        # Change the type of hand to soft, because the player has an ace
        player.hand = 'Soft'

        # Adds the number of aces to the first item in the list, and 10 + the number of aces to the second item
        # Theses are the only two valid scores when you have any number of aces
        player.score[0] += number_of_aces
        player.score[1] += number_of_aces + 10

    if max(player.score) > 21:  # If the player has an ace but his first score is over 21, his hand become hard again

        player.hand = 'Hard'


def draw_card(deck, player):

        player.cards.append(deck.pop(0))  # Draw the first card of the deck and deletes it from the list


def choose_bets(player):

    while player.bet not in range(2, player.money + 1):  # The player can only bet between 2$ and his money

        player.bet = int(input('{}, enter your bet, you have {}$: '.format(player.name, player.money)))

    player.money -= player.bet  # Subtract the bet to the player's money


def hit_or_stand(choice=''):  # Let the player choose if they hit or stand

    while choice not in ['Hit', 'Stand']:

        choice = input('Hit or Stand ? ')

    return choice == 'Hit'


def display_cards(player):  # Used to display all the cards of the players in the same format

    print('{} cards are {}\n'
          # Use "playerNames'" if the player name finishes with an s otherwise use "playerName's" format
          .format(player.name + ("'" if player.name.endswith('s') else "'s"),
                  # Displays the list of the players cards
                  str(player.cards).replace('[', '').replace("'", '').replace(']', '')))


def first_turn(Players, Dealer, deck):  # First turn of the game

    for player in Players:

        choose_bets(player)  # Let each player choose his bet

    print()

    for i in range(2):  # Distributes 2 cards

        for player in Players:  # To each player

            draw_card(deck, player)

            score(player)

            display_cards(player)

            time.sleep(1)  # Wait 1s before the program continues

            if 21 in player.score:  # Check if the player has a blackjack

                print('You got a blackjack !')

        draw_card(deck, Dealer)

        if i == 0:

            # Displays only the first card of the dealer
            print("Dealer's card is {}\n".format(Dealer.cards[0]))


def insurance(Players, Dealer):

    if not Dealer.cards[0][0].isdigit():  # Check if it's a case where the player can take insurance

        for player in Players:

            if player.money < int(player.bet/2):  # If the player's money is under half his bet, he can't take insurance
                continue

            if input('Do you wish to take insurance {} (y/n)?'.format(player.name)) == 'y':

                player.insurance = True
                player.money -= int(player.bet/2)


def further_turns(Players, Dealer, deck):  # Manage all the next turns

    for player in Players:

        if 21 in player.score:
            continue

        print(player.name)
        print('Your score is {}'.format(player.score[0] if player.hand == 'Hard' else player.score))

        while hit_or_stand():  # Ask if the player want to hit until he doesn't

            draw_card(deck, player)

            score(player)

            display_cards(player)

            print('Your score is {}'.format(player.score[0] if player.hand == 'Hard' else player.score))

            if 21 in player.score:

                print('You got a blackjack !')

                break
                
            if min(player.score) > 21:  # Check if the player is busted

                print('You got busted')
                player.bet = 0  # The player loses his bet

                break

    display_cards(Dealer)  # Display the cards of the Dealer after all players have either gone bust or stand

    while dealer(Dealer):  # Check if the Dealer wants to hit or stand

        draw_card(deck, Dealer)

        score(Dealer)

        display_cards(Dealer)

        print("Dealer's score is {}".format(Dealer.score[0] if Dealer.hand == 'Hard' else Dealer.score))

        if min(Dealer.score) > 21:  # Check if the dealer is busted

            print('Dealer got busted')

            break


def end_of_game(Players, Dealer):  # Manage the end of the game

    # Takes the best score of the Dealer according to blackjack's rules
    score_dealer = Dealer.score[0] if Dealer.hand == 'Hard' else Dealer.score[1]

    for player in Players:

        # Takes the best score of the player
        score_player = player.score[0] if player.hand == 'Hard' else player.score[1]

        # If the Dealer is busted or the player score is above the Dealer score :
        if score_dealer > 21 or score_player >= score_dealer:

            # If the player has a blackjack he regains his bet and gains 1.5 * his bet
            if score_player == 21:

                player.money += int(2.5 * player.bet)

            # If the player score is equal to the dealer score, he regain his bet
            elif score_player == score_dealer:

                player.money += player.bet

            # The score of the player is above the dealer's score (but not equal to 21) or the dealer is busted,
            # The player regains his bet and gains 1 * his bet

            # If the player got busted, he will be in this category, but as his bet is 0, he will still loose
            else:

                player.money += 2 * player.bet

        player.bet = 0  # Reset the player bet


def reset_game(Players, Dealer):  # Reset all the values that need to be reset for the next game

    for player in Players:

        player.cards = []
        player.hand = 'Hard'

    Dealer.cards = []
    Dealer.hand = 'Hard'


def complete_game(Players, Dealer, deck):  # Manage the entire game

    first_turn(Players, Dealer, deck)

    insurance(Players, Dealer)  # Check for insurance after the first turn

    further_turns(Players, Dealer, deck)

    end_of_game(Players, Dealer)

    reset_game(Players, Dealer)

    for player in Players:  # Displays the money of each player at the end of the game

        print(player.name)
        print(str(player.money) + '$')
