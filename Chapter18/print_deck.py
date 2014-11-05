# DEck consists of a list of cards as an attribute.

class Card(object):
	''' Class card to represent a playing card '''
	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [None, 'Ace', '1', '2', '3', '4', '5', '6', '7', '8',
		'9', '10', 'Jack', 'Queen', 'King']

	def __init__(self, suit = 0, rank = 2):
		self.suit = suit
		self.rank = rank
	
	def __str__(self) :
		return 'Suit : %s  Rank : %s' % (Card.suit_names[self.suit],						Card.rank_names[self.rank])

class Deck(object):
	''' is a list of cards '''
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)

	def __str__(self):	
		res = []
		for card in self.cards:
			res.append( str(card))
		return '\n'.join(res)
dck = Deck()

print dck


