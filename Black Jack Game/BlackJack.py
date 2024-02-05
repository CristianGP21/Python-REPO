from Cards import Cards
from Deck import Deck
from Hand import Hand
from Chips import Chips


def take_bet(chips):
    while True:

        try:
            chips.bet = int(input('Please enter your bet: '))
        except:
            print('Invalid bet! \n'
                  'Please enter a valid bet: ')
            continue
        else:
            if chips.bet > chips.total:
                print(f"You do not have enough chips! You have {chips.total}")
            else:
                break


def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck, hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break


def show_some(player, dealer):
    # Show only ONE of the dealer's cards
    print("\nDealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])

    # Show all the cards
    print("\nPlayer's Hand")
    for card in player.cards:
        print(card)
    print("Total: " + str(player_hand.value))


def show_all(player, dealer):
    # show all the dealer's cards

    print("\nDealer's Hand", *dealer.cards, sep='\n')
    # calculate and display the value
    print(f"Value of Dealer's hand is: {dealer.value}")

    # show all the players cards
    print("\nPlayer's Hand", *player.cards, sep='\n')
    # calculate and display the value
    print(f"Value of Player's hand is: {player.value}")


def player_busts(player, dealer, chips):
    print("BUST PLAYER!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('PLAYER WINS!')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('BUST DEALER!')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('DEALER WINS!')
    chips.lose_bet()


def push(player, dealer):
    print('Dealer and player tie! PUSH')


################################################################################################
################################################################################################
# START THE GAME #
################################################################################################
################################################################################################

playing = True

# Set up the Player's chips
player_chips = Chips()

while True:
    # Print an opening statement
    print("Welcome to BlackJack!")


    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())


    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break


        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 or BUSTS
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand,dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

        # Inform Player of their chips total
        print("\n Player's total chips are: {}".format(player_chips.total))

    if player_chips.total == 0:
        print("You have run out of chips! Game over.")
        playing = False
        quit()

        # Ask to play again
    new_game = input("Would you like to play again? y/n: ")

    while new_game[0].lower() not in ['y', 'n']:
        print("Invalid input!")
        new_game = input("Would you like to play again? y/n: ")


    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing!")
        break

