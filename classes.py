values = {"Ace": 11, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
          "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}

suits = ("Cups", "Spades", "Diamonds", "Hearts")

ranks = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
         "Eight", "Nine", "Ten", "Jack", "Queen", "King")


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

    def deal_cards(self, player, number_of_cards):


        if number_of_cards == 1:

            player.cards.append(self.deck.get_one_card())

        if number_of_cards > 1:

            for i in range(0,number_of_cards):

                player.cards.append(self.deck.get_one_card())

    def get_cards(self):

        self.cards.append(self.deck.get_one_card())
        self.cards[0].face_up = False
        self.cards.append(self.deck.get_one_card())
        print(f"\nDealer's cards: {self.cards}\n")

    def reveal_card(self):

        self.cards[0].face_up = True
        print(f"\nDealer cards: {self.cards}\n")

        while self.sum_cards() <= 17:

            print("\nThe dealer hits")
            self.cards.append(self.deck.get_one_card())
            print(f"\nDealer's cards: {self.cards}")

            if self.sum_cards() > 21:

                print("\nThe dealer busted!!!")
                break

        else:

            print("\nThe dealer stays")


class Player:

    def __init__(self):

        self.cards = []
        self.money = 1000
        self.round_bet = 0
        self.is_splited = False
