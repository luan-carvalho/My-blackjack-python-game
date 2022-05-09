# This is the game it self
from classes import *
# Game logic

# 1 Create the dealer and the player

dealer = Dealer()
player = Player()
min_bet = 300


while player.has_money(min_bet):

    # 2 The  player bets and the dealer deals two cards for the player and for himself

    player.bet(min_bet)
    # dealer.deal_cards(player, 2)
    player.cards = [Card("Ace", "Spades"), Card("Ten", "Hearts")]
    dealer.get_cards()

    # 3 Check if the player has a blackjack hand (if yes, the game ends and the player wins 3:2)

    if dealer.check_blackjack(player):

        if repeat(player, dealer):

            continue

        else:

            break

    # 4 The player chooses his move(hit, stay, double-down or split)

    player.play(dealer)

    if has_busted(player):

        if repeat(player, dealer):

            continue

        else:

            break

    # 5 Dealer reveals his card

    dealer.reveal_card()

    if has_busted(dealer):

        player.money += player.round_bet*2
        print(f"\nPlayer money: {player.money}")

        if repeat(player, dealer):

            continue

        else:

            break

    # 7 Check the winner

    dealer.check_win(player)

    # 8 The player chooses to repeat or not

    if repeat(player, dealer):

        continue

    else:

        break

print("\nBye-bye!!!")
