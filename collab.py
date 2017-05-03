from math import*
from decimal import Decimal

### Distances

def nth_root(value, n_root):
    root_value = 1/float(n_root)
    return round (Decimal(value) ** Decimal(root_value), 3)

def minkowski_distance(ratings, current, other, p_value = 3):
    return nth_root(sum([abs(ratings[current][item] - ratings[other][item]) for item in ratings[current] if item in ratings[other]]), p_value)

def manhattan_distance(ratings, current, other):
	common = len([ratings[current][item] for item in ratings[current] if item in ratings[other]])
	if common == 0:
		return 0
	manhattan_sum = sum([abs(ratings[current][item] - ratings[other][item]) for item in ratings[current] if item in ratings[other]])
	return manhattan_sum

### Algorithms

def top_similar(ratings, current, top = 5, similarity_function = None):
    scores = [(similarity_function(ratings, current, other), other) for other in ratings if other != current]
    scores.sort()
    scores.reverse()
    return scores[0:top]

def recommend(ratings, current, min_rating, similarity_function = None):
	totals = {}
	similarity_sums = {}
	for other in ratings:
		if other == current:
			continue
		sim = similarity_function(ratings, current, other)
		if sim <= 0.2:
			continue
		for item in ratings[other]:
			if item not in ratings[current] or ratings[current][item] < min_rating:
				totals.setdefault(item, 0)
				totals[item] += ratings[other][item] * sim
				similarity_sums.setdefault(item, 0)
				similarity_sums[item] += sim
	rankings = [(totals[item] / similarity_sums[item], item) for item in totals.keys()]
	rankings.sort()
	rankings.reverse()
	return rankings
