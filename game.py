# This is the game it self
from classes import *
from time import sleep

def screen_break():

    print("\n")
    print("#"*100)
    print("\n")

# Game logic

# 1 Create the dealer and the player

dealer = Dealer()
player = Player()

screen_break()

print("Welcome to the Monkey's cassino!! This is a Blackjack table.\n\nThe minimal bet is $300.")
print(f"\nYou have ${player.money}")

screen_break()

min_bet = 300

while player.money > min_bet:

    # 2 The  player bets and the dealer deals two cards for the player

    player.bet(min_bet)

    screen_break()

    sleep(2)

    print("\nDealing your cards...")

    sleep(2)

    dealer.deal_cards(player, 2)

    # 3 Check blackjack

    screen_break()

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

    screen_break()

    # 5 The player chooses his move(hit, stay, double-down or split)

    print("\nYour action!!!")

    sleep(2)

    player.play(dealer)

    if player.total > 21:

        screen_break()
        sleep(2)

        if repeat(player, dealer):

            continue

        else:

            break

    # 6 Dealer reveals his card

    screen_break()

    print("\nRevealing dealer's card")

    sleep(2)

    dealer.reveal_card(player)

    if dealer.total > 21:

        screen_break()
        sleep(2)

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
else:

    print("Hey, you don't have money to stay in the game.")

print("\nBye-bye!!!")
