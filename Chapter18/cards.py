class Card(object):
	''' Class card to represent the standard playing card '''
	''' It's attributes are suits and ranks '''
	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
			'8', '9', '10', 'Jack', 'Queen', 'Kinf']
	
	def __init__(self, suit = 0, rank = 2):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return '%s of %s' % (Card.rank_names[self.rank], 
					Card.suit_names[self.suit])


print Card(1,10)

