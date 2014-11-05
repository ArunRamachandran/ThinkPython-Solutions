class Card(object):
	''' class card to represent a playing card '''
	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8',
			'9', '10', 'Jack', 'Queen', 'King']

	def __init__(self, suit = 0, rank = 2):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return 'Suit : %s   Rank : %s' % (Card.suit_names[self.suit], Card.rank_names[self.rank])

	def __cmp__(self,other):
		''' first priority to Suit and then Rank '''
		# check suits
		if self.suit > other.suit :
			return 1
		if self.suit < other.suit :
			return -1
	
		# check Ranks
		if self.rank > other.rank :
			return 1
		if self.rank < other.rank :
			return -1
	
		#If suits and ranks are the same, then it's a tie..!!
		return 0

c = Card(3,10)
print Card(1,10)
d = Card(3,2)
print d

case = cmp(c,d)
print case
