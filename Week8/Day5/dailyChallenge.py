# import random
#
# suit_list = ['Hearts','Diamonds','Clubs','Spades']
# class Cards:
#   def __init__(self, suit):
#       while suit not in suit_list:
#         suit = input('please choose Heart,Diamonds,Clubs or Spades').lower().capitalize()
#       self.suit  = suit
#       self.cards = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
#
# class Deck:
#   def __init__(self,Cards_l):
#     self.cards = []
#     for cards in Cards_l:
#       i = 0
#       for card in cards.cards:
#         self.cards.append({cards.suit:card})
#     print(self.cards)
#
#   def shuffle_deck(self):
#     print(self.cards)
#     random.shuffle(self.cards)
#     print(self.cards)
#     return self
#
#   def deal(self):
#     dealt_card = random.choice(self.cards)
#     self.cards.remove(dealt_card)
#     return dealt_card
#
# cards_1 = Cards('Hearts')
# cards_2 = Cards('Diamonds')
# cards_3 = Cards('Clubs')
# cards_4 = Cards('Spades')
#
# cards_list = [cards_1,cards_2,cards_3,cards_4]
# deck = Deck(cards_list)
#
# deck.shuffle_deck()
# print(deck.deal())

suit_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
value_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck_dict = {}
deck_list = [{}, {}, {}, {}]

class Card():
    def __init__(self, suit_list, value_list, deck_dict):
        self.suit_list = suit_list
        self.value_list = value_list
        self.deck_dict = deck_dict
class Deck():
    def __init__(self, suit_list, value_list, deck_dict, deck_list):
        self.suit_list = suit_list
        self.value_list = value_list
        self.deck_dict = deck_dict
        self.deck_list = deck_list
    def shuffle(self):
            for value in value_list:
                self.deck_list[0][value] = self.suit_list[0]
                self.deck_list[1][value] = self.suit_list[1]
                self.deck_list[2][value] = self.suit_list[2]
                self.deck_list[3][value] = self.suit_list[3]
                deck_list[0].update(deck_list[1])
                deck_list[0].update(deck_list[2])
                deck_list[0].update(deck_list[3])


    # def deal(self):
deckOne = Deck(suit_list, value_list, deck_dict, deck_list)
deckOne.shuffle()
print(len(deck_list[0]))
print(deck_list[0])