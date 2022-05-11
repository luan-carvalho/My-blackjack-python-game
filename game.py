# This is the game it self
from classes import *
from time import sleep

# Game logic

# 1 Create the dealer and the player

print("\nWelcome to the Monkey's cassino!! This is a Blackjack table. The minimal bet is $300.")
print("\nYou have $1000")

dealer = Dealer()
player = Player()

min_bet = 300


while player.money > min_bet:

    # 2 The  player bets and the dealer deals two cards for the player

    player.bet(min_bet)

    sleep(2)

    print("\nDealing your cards...")

    sleep(2)

    dealer.deal_cards(player, 2)

    # 3 Check blackjack

    sleep(2)

    if dealer.check_blackjack(player):

        if repeat(player, dealer):

            continue

        else:

            break

    # 4 Dealer deals his cards

    print("\nDealing dealer's cards...")

    sleep(2)

    dealer.get_cards()

    # 5 The player chooses his move(hit, stay, double-down or split)

    print("\nYour action!!!")

    sleep(2)

    player.play(dealer)

    if player.total > 21:

        if repeat(player, dealer):

            continue

        else:

            break

    # 6 Dealer reveals his card

    print("\nRevealing dealer's card")

    sleep(2)

    dealer.reveal_card(player)

    if dealer.total > 21:

        if repeat(player, dealer):

            continue

        else:

            break

    # 7 Check the winner

    sleep(2)

    dealer.check_winner(player)

    # 8 The player chooses to repeat or not

    sleep(2)

    if repeat(player, dealer):

        continue

    else:

        break
else:

    print("Hey, you don't have money to stay in the game.")

print("\nBye-bye!!!")
