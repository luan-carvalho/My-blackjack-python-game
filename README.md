![♥️_Blackjack_♠️](https://user-images.githubusercontent.com/55687321/168387175-5fef5eb1-e057-4db4-9c31-81a9f18dbd3f.png)

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

A text-based Blackjack `Python` game.

# Content guide

- [How to install and play it](#How-to-install-and-play-it)
- [The goal of blackjack](#The-goal-of-Blackjack)
- [The deck and the cards](#The-deck-and-the-cards)
- [The game logic](#The-game-logic)
- [Payouts](#Payouts)
- [Player actions](#Player-actions)
- [Ace value](#Ace-value)

# How to install and play it

- To play it, you must have Python installed on your machine (you can download it [here](https://www.python.org/downloads/))

- After installing, you need to download this repository into your machine

![Screen Shot 2022-05-15 at 01 12 17](https://user-images.githubusercontent.com/55687321/168457048-c1617234-558c-4941-b390-21aa9e03a0b7.png)

- Unzip the file, open the folder and open the "game.py" file

![Screen Shot 2022-05-15 at 01 15 06](https://user-images.githubusercontent.com/55687321/168457135-70c6a4eb-1b15-485c-866f-9fab9dcb13aa.png)

- It will open Python IDLE and you can run it (search for similar options on Windows)

![Screen Shot 2022-05-15 at 01 16 15](https://user-images.githubusercontent.com/55687321/168457153-1ee4f76b-a7f9-4935-829b-fc26b360da57.png)

![Screen Shot 2022-05-15 at 01 17 11](https://user-images.githubusercontent.com/55687321/168457159-6d1911ca-7ff4-4e46-a59d-4515b8ecdb56.png)

- Check the game logic and rules on the next topics

# The goal of Blackjack

- In Blackjack, the main goal is to get closer to 21 than the dealer without going over 21

- If the dealer gets closer to 21 than the player, the player loses

- If the player goes over 21, he loses

# The deck and the cards

- The Blackjack's deck has 4 suits with 13 cards each

- Each card has a point value

- 2-10s are pointed by their face value (ex: Two of Spades is going to worth
  2 points)

- Jacks, Queens and Kings are going to worth 10 points each
- Aces can worth 1 or 11, depending on what is best for the hand

# The game logic

- The player starts with $1500 and have to place a bet

- The minimal bet is $300

- After betting, the dealer deals two cards to the player and to himself

- One of dealer's card is face-down and the other is face-up

- Then, the player can choose between the following moves:

  - `Hit`
  - `Stand`
  - `Double-down`
  - `Split`

- After that, the dealer reveals his face-down card

- If the dealer has less than 17 points, he must hit until gets a 17 or greater

- When he gets 17 points, he must stand

# Payouts

- When the player beats the dealer, he wins and gets an equal amount of what he just bet

- If the player has the same amount than the dealer's, he just gets his money back

- If the dealer gets closer to 21 than the player, the player loses his entire bet

- If the player gets an ace and a ten-value card in his first two cards, he wins automatically and gets paid 3:2. It's called a `Blackjack`

# Player actions

- Hitting: The player gets one more card

![Screen Shot 2022-05-15 at 02 16 10](https://user-images.githubusercontent.com/55687321/168458375-2a483a53-7a21-4f2f-b739-770ec2af1224.png)

- Standing: The player chooses to stay with his cards and doesn't get more cards

![Screen Shot 2022-05-15 at 02 15 47](https://user-images.githubusercontent.com/55687321/168458370-cdf8af6e-f9cf-4a0e-887a-03ff60bb39a1.png)

- Double-down: The player doubles hist bet and get one last card (only allowed on the first move)

![Screen Shot 2022-05-15 at 02 16 48](https://user-images.githubusercontent.com/55687321/168458381-5b89fe90-2c1d-4795-b022-1f0ebba86bfd.png)

- Splitting: If the player gets two cards of the same rank, he can create a new hand with his cards and play with more than one hand

  - It's only allowed if the player can pay another bet of the same value of the first bet for the new hand
  - The player can split his cards up to a maximun of 3 times (to play a total of 4 hands)

![Screen Shot 2022-05-15 at 02 27 58](https://user-images.githubusercontent.com/55687321/168458556-c4dd7e2a-5133-40ee-9c08-8e459b04663c.png)

# Ace value

- In this game, the ace can worth 1 or 11, depending on what is best for the hand

- When the ace doesn't make the hand bust, it's going to worth 11

- If the ace makes the hand bust, it automatically is going to worth 1

- If the hand has an ace and another card makes the hand bust, the ace will automatically worth 1

![Screen Shot 2022-05-15 at 02 34 40](https://user-images.githubusercontent.com/55687321/168458711-ccaf9da0-a74d-44db-8095-89d6b8440e77.png)
