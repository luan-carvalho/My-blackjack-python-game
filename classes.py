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

            for i in range(0, number_of_cards):

                player.cards.append(self.deck.get_one_card())

        print(f"\nPlayer cards: {player.cards}")

    def get_cards(self):

        self.cards.append(self.deck.get_one_card())
        self.cards[0].face_up = False
        self.cards.append(self.deck.get_one_card())
        print(f"\nDealer's cards: {self.cards}")

    def reveal_card(self):

        self.cards[0].face_up = True
        print(f"\nDealer cards: {self.cards}\n")

        while sum_cards(self.cards) <= 17:

            print("\nThe dealer hits")
            self.cards.append(self.deck.get_one_card())
            print(f"\nDealer's cards: {self.cards}")

            if sum_cards(self.cards) > 21:

                print("\nThe dealer busted!!!")
                break

        else:

            print("\nThe dealer stays")

    def check_blackjack(self, player):

        if sum_cards(player.cards) == 21:

            print("\nWinner winner chicken dinner!!!!")

            player.money += player.round_bet*2.5

            print(f"\nPlayer money: {player.money}")

    def check_win(self, player):

        player.money += player.round_bet*2


class Player:

    def __init__(self):

        self.cards = []
        self.money = 1000
        self.round_bet = 0
        self.is_splited = False

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

    
    def player(self, dealer: Dealer):

        while True:

            try:

                print("\n1 - Hit\n2 - Stay\n3 - Double-down\n4-Split")

                move = int(input("\nYour move: "))

                if not(move in [1,2,3,4]):

                    print("\nHey, choose a valid move.")
                    x = 1/0 #forcing an error

                elif move == 3 and self.bet > self.money:

                    print("\nHey, you don't have money for a double-down.")
                    x = 1/0

                elif move == 4 and (self.cards[0].rank == self.cards[1].rank or self.money < self.bet):

                    print("\nHey, you can't split. Check your hand or your money.")
                    x = 1/0

            except:

                continue
                
            else:

                if move == 1:

                    dealer.deal_cards(self, 1)
                    print(f"\nPlayer cards: {self.cards}")

                    while True:

                        print("1 - Hit\n2 - Stay")

                        try:

                            move = int(input("\nYour move: "))

                            if not(move in [1,2]):

                                print("\nHey, enter a valid move.")
                                x = 1/0

                        except:

                            continue

                        else:

                            if move == 1:

                                dealer.deal_cards(self, 1)
                                print(f"\nPlayer cards: {self.cards}")
                                continue
                            
                            if move == 2:

                                print("\nthe player stays.")
                                print(f"\nPlayer cards: {self.cards}")
                                break

                elif move == 2:

                    print("\nThe player stays.")
                    break

                elif move == 3:

                    print(f"\nThe player doubles-down.\nPlayer money: {self.money}")
                    self.money -= self.round_bet
                    self.round_bet = self.round_bet*2
                    dealer.deal_cards(self, 1)
                    print(f"\nPlayer cards: {self.cards}")

                    if sum_cards(self.cards) > 21:

                        print("\nThe player busted!!!")
                        break

                elif move == 4:

                    pass