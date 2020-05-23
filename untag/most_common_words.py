def sol(literatureText, wordsToExclude):
	# Edge case handling
	if not literatureText or literatureText == '': return []

	excluded = set(wordsToExclude)
	dic = {}

	# Remove puncuations
	for item in ",./?!';:":
		literatureText = literatureText.strip(item, " ")
	literatureText = literatureText.split()

	# If text contains no valid word (only punctuations)
	if not literatureText: return []

	for word in literatureText:
		if word not in excluded:
			word = word.lower()
			if word not in dic: 
				dic[word] = 1
			else:
				dic[word] += 1
	print dic

	# if len(count) == 0: return []

	ma = max(dic.values())	
	ret = []
	for key, val in dic.items():
		if val == ma:
			ret.append(key)
	return ret
text = "Jack and Jill went to the market to buy bread and cheese. Cheese is Jack's and Jill's favorite food."
wordsToExclude = ["and", "he", "the", "to", "is", "Jack", "Jill"]
print (sol(text, wordsToExclude))