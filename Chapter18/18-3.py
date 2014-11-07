class Cards(object):
	''' class cards to represrent playing cards '''
	suit_names = ['clubs', 'diamonds', 'hearts', 'spades']
	rank_names = [None, 'Ace', '1', '2', '3', '4', '5', '6', '7', '8',
			'9', '10', 'Jack', 'Queen', 'King']
	def __str__(self):
		return '%s %s' % (Cards.suit_names[self.suit],
				  Cards.rank_names[self.rank])
	def __init__(self,suit = 0, rank = 2):
		self.suit = suit
		self.rank = rank

class Deck(object):
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1,15):
				card = Cards(suit,rank)
				self.cards.append(card)

	def __str__(self):
		res = []
		for card in self.cards:
			res.append(str(card))
		return '\n'.join(res)

	def pop_card(self):
		return self.cards.pop()

	def add_card(selif, card):
		self.cards.append(card)	

class Hand(Deck):
	''' represents a hand of cards '''
	def __init__(self,label = ''):
		self.cards = []
		self.label = label

	def move_cards(self,hand,num):
		for in range(num):
			hand.add_card(self.pop_card())
ck = Cards(0,2)
print ck

hand = Deck()
print hand
