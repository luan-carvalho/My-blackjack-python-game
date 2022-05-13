![_♠️_Blackjack_♦️](https://user-images.githubusercontent.com/55687321/168382865-9c5d6171-ef92-4e6e-b1ac-87bb2fdddd34.png)

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

A text-based Blackjack `Python` game.

# Content guide

- [How to install and play it](#How-to-install-and-play-it)
- [The goal of blackjack](#The-goal-of-Blackjack)
- [The deck and the cards](#The-deck-and-the-cards)
- [The game logic](#The-game-logic)
- [Payouts](#Payouts)
- [Player actions](#Player-actions)


# The goal of Blackjack

- In Blackjack, the main goal is to get closer to 21 than the dealer without going over 21
- If the dealer gets closer to 21 than the player, the player loses
- If the player goes over 21, he loses

# The deck and the cards

- The Blackjack's deck has 4 suits with 13 cards each
- Each card has a point value
- 2-10s are pointed by their face value (ex: Two of Spades is going to worth 2 points)
- Jacks, Queens and Kings are going to worth 10 points each
- Aces can worth 1 or 11, depending on what is best for the hand

# The game logic

- The player starts with $1500 and have to place a bet
- The minimal bet is $300
- After betting, the dealer deals two cards to the player and to himself
- One of dealer's card is face-down and the other is face-up
- Then, the player can choose between the following moves:
    - Hit
    - Stand
    - Double-down
    - Split
- After that, the dealer reveals his face-down card
- If the dealer has less than 17 points, he must hit until gets a 17 or greater
- When he gets 17 points, he must stand

# Payouts

- When the player beats the dealer, he wins and gets an equal amount of what he just bet
- If the player has the same amount than the dealer's, he just get his money back
- If the dealer gets closer to 21 than the player, the player loses his entire bet
- If the player gets an ace and a ten-value card in his first two cards, he wins automatically and gets paid 3:2. It's called a Blackjack.

# Player actions
