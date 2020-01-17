'''
Google phone interview
"An N-ary tree was given with their level of stickiness on the edges. If the 
water is falling from the root, find the min time taken to wet the whole tree."

Follow-ups:
1. Use a stack instead of recursion
2. Graph instead of tree
3. Design API: addNode(), updateNode(), deleteNode()

Wet Tree:
• Complexity:
	○ O(n)
• Topics:
	○ tree
对于树来说，是一个找longest path(with weight)的问题。DFS解决，longest path需要花最长的时
间去wet，决定了整个树wet所需的时间。
原题用DFS with recursion解，特点是maxPath(node)必然return以该node为root的subtree的
longest path、某种意义上来说是从leaf逐渐回到root，因此不需要pass in任何长度。
DFS with iteration是从root到各个leaf, 区别在于需要keep一个global max，以及每次push一个
node到stack的时候也需要传递一个root到该node的path length。

Wet Graph:
• Complexity:
	○ O(ElogV) - E: # edges, V: # vertices
• Topics:
	○ tree
Assume all nodes are connected.
wet graph随机给root，和tree的区别在于：tree从root到每个leaf只有一个unique path，而graph
里可能有多个path，而我们需要找到的是所有min path里面最长的那个path，which decides wet整个
graph所需的时间。
因此这个问题变成用dijkstra找到所有node的shortest path的问题，最后return所有shortest paths
里最长的那个。while(min_heap)正常退出即guarantee all nodes visited with their 
shortest path_len found.
dijsktra细节，refer to: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-using-priority_queue-stl/
'''

# class Node:
#	 def __init__(self, val):
#		 self.val = val 
#		 self.children = [] # stores tuples: (node, edge_len)

# recursive
def wetTree(root):
	# 不查not root，maxPath()可handle

	def maxPath(node):
		if not node:
			return 0
		paths = []
		for child, edge_len in node.children:
			paths.append(maxPath(child) + edge_len)
		return max(paths)
	return maxPath(node)

# iterative
def wetTree(root):
	if not root: 
		return 0

	# stack stores tups: (node, path_len from root)
	max_, stack = 0, [(root, 0)]
	while stack:
		curr, path_len = stack.pop()
		if not curr.chldren: # if curr is leaf
			max_ = max(path_len, max_)
		else:
			for child, edge_len in curr.children:
				stack.append((child, path_len + edge_len))
	return max_

# class Vertice:
#	 def __init__(self, val):
#		 self.val = val 
#		 self.neighbors = [] # stores tuples: (vertice, edge_len) 

# wet graph with dijkstra
import heapq

def wetGraph(node):
	if not node:
		return 0

	visited = set()
	min_heap = [(0, node)]
	max_ = 0

	while min_heap:
		path_len, curr = heapq.heappop(min_heap)
		# if curr has been visited, continue
		if curr in visited:
			continue
		else:
			visited.add(curr)
			max_ = max(path_len, max_)
			for neighbor, edge_len in curr.neighbors:
				if neighbor not in visited:
					heapq.append(min_heap, (path_len + edge_len, neighbor))
	return max_
