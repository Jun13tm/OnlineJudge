'''
LC236 类似
'''

def sol(pairs, p1, p2):
	dic = {}
	for boss, employee in pairs:
		dic[employee] = boss
	
	path = [p1]
	curr = p1
	while curr in dic:
		path.append(dic[curr])
		curr = dic[curr]
	
	set_ = set()
	set_.add(p2)
	curr = p2
	while curr in dic:
		set_.add(dic[curr])
		curr = dic[curr]

	print(set_)
	print(path)

	# The first character shows up in the path is the loweset ancestor
	for item in path:
		if item in set_:
			return item
	return -1
