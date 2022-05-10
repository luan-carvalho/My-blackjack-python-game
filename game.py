# This is the game it self
from classes import *
from time import sleep


def screen_break():

    print("\n")
    print("*"*100)
    print("\n")

# Game logic

# 1 Create the dealer and the player

screen_break()

print("\nWelcome to the Monkey's cassino!! This is a Blackjack table. The minimal bet is $300.")
print("\nYou have $1000")

dealer = Dealer()
player = Player()
min_bet = 300


while player.has_money(min_bet):

    # 2 The  player bets and the dealer deals two cards for the player and for himself

    screen_break()

    player.bet(min_bet)

    screen_break()

    sleep(2)

    print("\nDealing your cards...")

    sleep(2)

    dealer.deal_cards(player, 2)

    screen_break()

    sleep(2)

    if dealer.check_blackjack(player):

        screen_break()

        if repeat(player, dealer):

            continue

        else:

            break

    print("\nDealing dealer's cards...")

    sleep(2)

    dealer.get_cards()

    # 4 The player chooses his move(hit, stay, double-down or split)

    screen_break()

    sleep(2)

    player.play(dealer)

    if player.total > 21:
        
        if repeat(player, dealer):

            continue

        else:

            break

    
    # 5 Dealer reveals his card

    screen_break()

    print("\nRevealing dealer's card")

    sleep(2)

    dealer.reveal_card(player)

    if dealer.total > 21:

        if repeat(player, dealer):

            continue

        else:

            break

    # 7 Check the winner

    screen_break()

    sleep(2)

    dealer.check_winner(player)

    # 8 The player chooses to repeat or not

    screen_break()

    sleep(2)

    if repeat(player, dealer):

        continue

    else:

        break

print("\nBye-bye!!!")
