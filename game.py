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
# 4 The player chooses his move(hit, stay, double-down or split)
# 5 Check if the player busts
# 6 Dealer reveals his card
# 7 The dealer stays or hit
# 8 Check the winner
# 9 The player chooses to repeat or not  
