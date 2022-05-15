values = {"Ace": 11, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
          "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}

suits = ("Cups", "Spades", "Diamonds", "Hearts")

ranks = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
         "Eight", "Nine", "Ten", "Jack", "Queen", "King")


def repeat(player, dealer):

    while True:

        try:

            print("\nDo you want to play again?\n\n1 - Yes\n2 - No")

            ask = int(input("\nYour choice: "))

            if not(ask in [1, 2]):

                print("\nHey, enter a valid choice!")

        except:

            continue

        else:

            if ask == 1:

                player.cards = []
                player.total = 0
                dealer.cards = []
                dealer.total = 0
                dealer.deck = Deck()
                return True

            elif ask == 2:

                return False


class Card:

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit
        self.value = values[rank]
        self.face_up = True
        self.change_value = False  # Attribute to check if an ace has been changed to 1

    def __str__(self):

        if self.face_up == True:

            return f"{self.rank} of {self.suit}"

        else:

            return "This card is face-down"

    def __repr__(self):

        if self.face_up == True:

            return f"{self.rank} of {self.suit}"

        else:

            return "This card is face-down"


class Deck:

    def __init__(self):

        import random

        self.all_cards = []

        for suit in suits:

            for rank in ranks:

                self.all_cards.append(Card(rank, suit))

        random.shuffle(self.all_cards)

    def get_one_card(self):

        my_card = self.all_cards.pop(0)
        return my_card


class Dealer:

    def __init__(self):

        self.deck = Deck()
        self.cards = []
        self.total = 0  # Attribute to track the hand total value

    def deal_cards(self, player, number_of_cards):

        if number_of_cards == 1:

            player.cards.append(self.deck.get_one_card())
            player.total += player.cards[-1].value

            # list with all aces that are not 1 yet
            aces = [card for card in player.cards if card.rank ==
                    "Ace" and card.change_value == False]

            while player.total > 21 and len(aces) != 0:

                print(f"\nYour cards: {player.cards} ({player.total})")

                player.total -= 10
                aces[-1].change_value = True

                print(f"\n## Ace value changed to 1 ##")

            else:

                print(f"\nYour cards: {player.cards} ({player.total})")

        if number_of_cards > 1:

            for i in range(0, number_of_cards):

                player.cards.append(self.deck.get_one_card())
                player.total += player.cards[-1].value

            print(f"\nYour cards: {player.cards} ({player.total})")

    def split_dealing(self, player, hand):

        player.cards[hand-1].append(self.deck.get_one_card())
        player.total[hand-1] += player.cards[hand-1][-1].value

        aces = [card for card in player.cards[hand-1]
                if card.rank == "Ace" and card.change_value == False]

        while player.total[hand-1] > 21 and len(aces) != 0:

            print(
                f"\nHand {hand}: {player.cards[hand-1]} ({player.total[hand-1]})")

            player.total[hand-1] -= 10
            aces[-1].change_value = True

            print("\n## Ace value changed to 1 ##")

        else:

            print(
                f"\nHand {hand}: {player.cards[hand-1]} ({player.total[hand-1]})")

    def get_cards(self):

        self.cards.append(self.deck.get_one_card())
        self.cards[0].face_up = False
        self.cards.append(self.deck.get_one_card())
        self.total += sum([card.value for card in self.cards])
        print(f"\nDealer cards: {self.cards}")

    def reveal_card(self, player):

        import time

        aces = [card for card in self.cards if card.rank ==
                "Ace" and card.change_value == False]

        self.cards[0].face_up = True
        print(f"\nDealer cards: {self.cards} ({self.total})")

        if self.total and len(aces) > 21:

            self.total -= 10
            print("\n## Ace value changed to 1 ##")
            print(f"\nDealer cards: {self.cards} ({self.total})")

        while self.total <= 16:

            aces = [card for card in self.cards if card.rank ==
                    "Ace" and card.change_value == False]

            time.sleep(2)

            print("\nThe dealer hits")
            self.cards.append(self.deck.get_one_card())
            self.total += self.cards[-1].value
            print(f"\nDealer cards: {self.cards} ({self.total})")

            while self.total > 21 and len(aces) != 0:

                self.total -= 10
                aces[-1].change_value = True
                print("\n## Ace value changed to 1 ##")
                print(f"\nDealer cards: {self.cards} ({self.total})")

            else:

                if self.total > 21:

                    print("\nThe dealer busted!!!")
                    player.round_bet += player.round_bet*2
                    print(f"\nYour money: ${player.money}")
                    break

        else:

            print("\nThe dealer stands")

    def check_blackjack(self, player):

        if player.total == 21:

            print("\nWinner winner chicken dinner!!!!")

            player.money += player.round_bet*2.5

            print(f"\nYour money: ${player.money}")

            return True

        else:

            return False

    def check_winner(self, player):

        # checking when the player did not split hands

        if type(player.total) == int:

            if player.total > self.total:

                print("\nYou win!!!")
                player.money += player.round_bet*2
                print(f"Your money: ${player.money}")

            elif player.total < self.total:

                print("\nYou lose!!!")
                print(f"Your money: ${player.money}")

            elif player.total == self.total:

                print("\nPush!!!")
                player.money += player.round_bet
                print(f"Player money: ${player.money}")

        elif type(player.total) == list:

            hand = 1

            for total in player.total:

                if total == 0:

                    hand += 1
                    continue

                elif total > self.total:

                    print(f"\nHand {hand} wins!!!")
                    player.money += player.round_bet*2
                    print(f"\nYour money: ${player.money}")
                    hand += 1
                    continue

                elif total < self.total:

                    print(f"\nHand {hand} loses!!!")
                    print(f"\nYour money: ${player.money}")
                    hand += 1
                    continue

                elif total == self.total:

                    print(f"\nHand {hand} push!!!")
                    player.money += player.round_bet
                    print(f"\nYour money: ${player.money}")
                    hand += 1
                    continue


class Player:

    def __init__(self):

        self.cards = []
        self.money = 1500
        self.round_bet = 0
        self.total = 0  # Attribute to track the hand total value

    def bet(self, min_bet):

        while True:

            try:

                bet = int(input("\nEnter your bet: "))

                if bet > self.money:

                    print("\nHey, you don't have enough money.")
                    x = 1/0  # forcing an error

                elif bet < min_bet:

                    print("\nHey, your bet is lesser than the minimal.")
                    x = 1/0

            except:

                continue

            else:

                self.round_bet = bet
                self.money -= self.round_bet
                print(
                    f"\nYour money: ${self.money}\nYour round bet: ${self.round_bet}")
                break

    def play(self, dealer: Dealer):

        print(f"Your cards: {self.cards} ({self.total})")

        while True:

            try:

                if self.cards[0].rank == self.cards[1].rank:

                    print("\n1 - Hit\n2 - Stand\n3 - Double-down\n4 - Split")

                    move = int(input("\nYour move: "))

                    if not(move in [1, 2, 3, 4]):

                        print("\nHey, choose a valid move.")
                        x = 1/0  # forcing an error

                    elif move == 3 and self.round_bet > self.money:

                        print("\nHey, you don't have money for a double-down.")
                        x = 1/0

                    elif move == 4 and self.money < self.round_bet:

                        print(
                            "\nHey, you don't have money to split your hand.")
                        x = 1/0

                else:

                    print("\n1 - Hit\n2 - Stand\n3 - Double-down")

                    move = int(input("\nYour move: "))

                    if not(move in [1, 2, 3]):

                        print("\nHey, choose a valid move.")
                        x = 1/0  # forcing an error

                    elif move == 3 and self.round_bet > self.money:

                        print("\nHey, you don't have money for a double-down.")
                        x = 1/0

            except:

                continue

            else:

                if move == 1:

                    dealer.deal_cards(self, 1)

                    if self.total > 21:

                        print("\nYou busted!!!")
                        print(f"\nYour money: ${self.money}")
                        break

                    while True:

                        print("\n1 - Hit\n2 - Stand")

                        try:

                            move = int(input("\nYour move: "))

                            if not(move in [1, 2]):

                                print("\nHey, enter a valid move.")
                                x = 1/0

                        except:

                            continue

                        else:

                            if move == 1:

                                dealer.deal_cards(self, 1)

                                if self.total > 21:

                                    print("\nYou busted!!!")
                                    print(f"Your money: ${self.money}")
                                    break

                                continue

                            if move == 2:

                                print("\nYou stand.")
                                break

                    break

                elif move == 2:

                    print("\nYou stand.")
                    break

                elif move == 3:

                    self.money -= self.round_bet
                    self.round_bet = self.round_bet*2
                    print(
                        f"\nDouble-down!!\n\nYour money: ${self.money}\nYour round bet: ${self.round_bet}")
                    dealer.deal_cards(self, 1)

                    if self.total > 21:

                        print("\nYou busted!!!")
                        print(f"\nYour money: ${self.money}")
                        break

                    break

                elif move == 4:

                    self.total = [
                        self.cards[0].value, self.cards[1].value, 0, 0]

                    self.cards = [[self.cards[0]], [self.cards[1]]]

                    self.cards[0].append(dealer.deck.get_one_card())

                    self.total[0] += self.cards[0][-1].value

                    self.money -= self.round_bet

                    print(f"\nSplit!!!\n\nYour money: ${self.money}")

                    hand = 1

                    while True:

                        try:

                            print(
                                f"\nHand {hand}: {self.cards[hand-1]} ({self.total[hand-1]})")

                            if self.cards[hand-1][0].rank == self.cards[hand-1][1].rank and len(self.cards[hand-1]) == 2:

                                print("\n1 - Hit\n2 - Stand\n3 - Split")

                                move = int(
                                    input(f"\nYour move on hand {hand}: "))

                                if not(move in [1, 2, 3]):

                                    print("\nHey, enter a valid choice")
                                    x = 1/0

                                elif self.money < self.round_bet:

                                    print(
                                        "\nHey, you don't have money for splitting")
                                    x = 1/0
                            else:

                                print("\n1 - Hit\n2 - Stand")

                                move = int(
                                    input(f"\nYour move on hand {hand}: "))

                                if not(move in [1, 2]):

                                    print("\nHey, enter a valid choice")
                                    x = 1/0

                        except:

                            continue

                        else:

                            if move == 1:

                                dealer.split_dealing(self, hand)

                                if self.total[hand-1] > 21:

                                    print(f"\nHand {hand} busted!!!")
                                    self.total[hand-1] = 0

                                    if hand < len(self.cards):

                                        hand += 1
                                        self.cards[hand -
                                                   1].append(dealer.deck.get_one_card())
                                        self.total[hand -
                                                   1] += self.cards[hand-1][-1].value
                                        print(
                                            f"\nHand {hand}: {self.cards[hand-1]} ({self.total[hand-1]})")
                                        continue

                                    else:

                                        break

                                continue

                            elif move == 2:

                                if hand < len(self.cards):

                                    print(f"\nStand in hand {hand}")
                                    hand += 1
                                    self.cards[hand -
                                               1].append(dealer.deck.get_one_card())
                                    self.total[hand -
                                               1] += self.cards[hand-1][-1].value

                                    continue

                                else:

                                    print(f"\nStand in hand {hand}")
                                    break

                            elif move == 3:

                                self.cards.append([])
                                self.cards[-1] = [self.cards[hand-1][1]]
                                self.cards[hand-1] = [self.cards[hand-1][0]]
                                self.total[hand -
                                           1] = self.cards[hand-1][0].value
                                self.total[len(self.cards) -
                                           1] = self.cards[-1][0].value
                                self.money -= self.round_bet

                                self.cards[hand -
                                           1].append(dealer.deck.get_one_card())
                                self.total[hand -
                                           1] += self.cards[hand-1][-1].value

                                print("\nSplit!!!!")
                                print(f"\nYour money: ${self.money}")

                    break
