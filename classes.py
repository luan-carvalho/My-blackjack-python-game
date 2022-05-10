values = {"Ace": 11, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
          "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}

suits = ("Cups", "Spades", "Diamonds", "Hearts")

ranks = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
         "Eight", "Nine", "Ten", "Jack", "Queen", "King")


def sum_cards(cards):

    my_sum = 0

    for card in cards:

        my_sum += card.value

    return my_sum


def repeat(player, dealer):

    while True:

        try:

            print("\nDo you want to play again?\n1 - Yes\n2 - No")

            ask = int(input("Your choice: "))

            if not(ask in [1, 2]):

                print("Hey, enter a valid choice!")

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


def has_busted(player_or_dealer):

    if sum_cards(player_or_dealer.cards) > 21:

        return True

    else:

        return False


class Card:

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit
        self.value = values[rank]
        self.face_up = True

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
        self.total = 0 # Attribute to track the hand total value

    def deal_cards(self, player, number_of_cards):

        if number_of_cards == 1:

            player.cards.append(self.deck.get_one_card())
            player.total += player.cards[-1].value

        if number_of_cards > 1:

            for i in range(0, number_of_cards):

                player.cards.append(self.deck.get_one_card())
                player.total += player.cards[-1].value

        print(f"\nPlayer cards: {player.cards} ({player.total})")

    def get_cards(self):

        self.cards.append(self.deck.get_one_card())
        self.cards[0].face_up = False
        self.cards.append(self.deck.get_one_card())
        self.total += sum([card.value for card in self.cards])
        print(f"\nDealer cards: {self.cards}")

    def reveal_card(self):

        self.cards[0].face_up = True
        print(f"\nDealer cards: {self.cards}")

        while self.total <= 16:

            print("\nThe dealer hits")
            self.cards.append(self.deck.get_one_card())
            self.total += self.cards[-1].value
            print(f"\nDealer cards: {self.cards} ({self.total})")

            if self.total > 21:

                print("\nThe dealer busted!!!")
                break

        else:

            print("\nThe dealer stays")

    def check_blackjack(self, player):

        if self.total == 21:

            print("\nWinner winner chicken dinner!!!!")

            player.money += player.round_bet*2.5

            print(f"\nPlayer money: {player.money}")

            return True

        else:

            return False

    def check_win(self, player):

        # checking when the player did not split hands

        if player.total > self.total:

            print("\nPlayer wins!!!")
            player.money += player.round_bet*2
            print(f"Player money: {player.money}")

        elif player.total < self.total:

            print("\nThe player lost the game!!!")
            print(f"Player money: {player.money}")

        elif player.total == self.total:

            print("\nPush!!!")
            player.money += player.round_bet
            print(f"Player money: {player.money}")


class Player:

    def __init__(self):

        self.cards = []
        self.money = 1000
        self.round_bet = 0
        self.total = 0 # Attribute to track the hand total value

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
                break

    def play(self, dealer: Dealer):

        while True:

            try:

                print("\n1 - Hit\n2 - Stay\n3 - Double-down\n4 - Split")

                move = int(input("\nYour move: "))

                if not(move in [1, 2, 3, 4]):

                    print("\nHey, choose a valid move.")
                    x = 1/0  # forcing an error

                elif move == 3 and self.bet > self.money:

                    print("\nHey, you don't have money for a double-down.")
                    x = 1/0

                elif move == 4 and (self.cards[0].rank != self.cards[1].rank or self.money < self.bet):

                    print("\nHey, you can't split. Check your hand or your money.")
                    x = 1/0

            except:

                continue

            else:

                if move == 1:

                    dealer.deal_cards(self, 1)

                    if self.total > 21:

                        print("\nThe player busted!!!")
                        print(f"\nPlayer money: {self.money}")
                        break

                    while True:

                        print("\n1 - Hit\n2 - Stay")

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

                                    print("\nThe player busted!!!")
                                    print(f"Player money: {self.money}")
                                    break

                                continue

                            if move == 2:

                                print("\nthe player stays.")
                                print(
                                    f"\nPlayer cards: {self.cards} ({self.total})")
                                break

                    break

                elif move == 2:

                    print("\nThe player stays.")
                    break

                elif move == 3:

                    print(
                        f"\nThe player doubles-down.\nPlayer money: {self.money}")
                    self.money -= self.round_bet
                    self.round_bet = self.round_bet*2
                    dealer.deal_cards(self, 1)
                    print(
                        f"\nPlayer cards: {self.cards} ({self.total})")

                    if self.total > 21:

                        print("\nThe player busted!!!")
                        print(f"\nPlayer money: {self.money}")
                        break

                elif move == 4:

                    pass

    def has_money(self, min_bet):

        if self.money >= min_bet:

            return True

        else:

            print(f"\nYou don't have money for another hand.\nYour money: {self.money}\nMinimal bet: {min_bet}")
            return False
