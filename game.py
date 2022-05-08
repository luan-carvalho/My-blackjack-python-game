# This is the game it self
from classes import *
# Game logic

# 1 Create the dealer and the player

dealer = Dealer()
player = Player()
min_bet = 300

# 2 The  player bets and the dealer deals two cards for the player and for himself

player.bet(min_bet)
dealer.deal_cards(player, 2)
dealer.get_cards()

# 3 Check if the player has a blackjack hand (if yes, the game ends and the player wins 3:2)

dealer.check_blackjack(player)

# 4 The player chooses his move(hit, stay, double-down or split)

player.play(dealer)

# 5 Dealer reveals his card

dealer.reveal_card()

# 7 Check the winner

dealer.check_win(player)

# 8 The player chooses to repeat or not 

# if repeat(player, dealer):

#     continue

# else:

#     break
