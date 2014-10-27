
def len_hyp(x,y):
	#return 0.0 # to chcek whether the fn is properly wrkng or not
	sq = x ** 2 + y ** 2
	#return sq
	import math
	result = math.sqrt(sq)
	return result

len = len_hyp(3,4)
print len
