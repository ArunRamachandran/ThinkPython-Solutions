# DEck consists of a list of cards as an attribute.
''' Using inheritance '''
''' During inheritance, new class inheirts the methods of the existing 
	(parent) class. At the same time an inheritedd class (child)
	is also different from parent '''

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



class Hand(Deck):
	''' Represents a hand of playing cards '''
	''' Hand is inherited from Deck        '''
	def __init__(self,label = ''):
		self.cards = []
		self.label = label

hand = Hand('new hand')
print hand.cards
print hand.label
