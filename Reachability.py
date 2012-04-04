#Reachability

#Single Gold Star

#Define a procedure, reachable(graph, node), that takes as input a graph and a
#starting node, and returns a list of all the nodes in the graph that can be
#reached by following zero or more edges starting from node.  The input graph is
#represented as a Dictionary where each node in the graph is a key in the
#Dictionary, and the value associated with a key is a list of the nodes that the
#key node is connected to.  The nodes in the returned list may appear in any
#order, but should not contain any duplicates.


# def reachable(graph, node):
# 	nodes = []
# 	if node in graph:
# 		for key,values in graph.iteritems():
# 			if key == node:
# 				nodes.append(key)
# 			if node in values:
# 				for v in values:
# 					if v != node:
# 						nodes.append(v)
# 						nodes.append(key)
# 		return nodes

# def reachable(graph,node,seen = None):
# 	seen = seen or set()
# 	seen.add(node)
# 	reached = set(node)
# 	# print node
# 	adjacent = graph.get(node)
# 	# print adjacent

# 	if adjacent:
# 		reached.update(adjacent)
# 		for subnode in adjacent:
# 			if subnode in adjacent:
# 				if subnode not in seen:
# 					reached.update(reachable(graph,subnode,seen))
# 	return reached

# def reachable(graph,node):
	# seen = None
	# seen = seen or set()
	# seen.add(node)
	# reached = []
	# reached.append(node)
	# print node
	# adjacent = graph.get(node)
	# print adjacent

	# if adjacent:
	# 	reached.append(adjacent)
	# 	for subnode in adjacent:
	# 		if subnode in adjacent:
	# 			if subnode not in seen:
	# 				reached.append(reachable(graph,subnode))
	# return reached
			


def reachable(graph, node):
    visited = []
    if node in graph:
        for key, values in graph.iteritems():
        	if key == node:
        		visited.append(key)
        		for v in values:
        			# visited = reachable(graph,v)
        			visited.append(v)
        	if key not in visited:
        		if values == node:
        			visited.append(values)
        return visited






#For example,

graph = {'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['b', 'd'], 'd': ['a'], 'e': ['a']}

print reachable(graph, 'a')
#>>> ['a', 'c', 'd', 'b']

#print reachable(graph, 'd')
#>>> ['d', 'a', 'c', 'b']

print reachable(graph, 'e')
#>>> ['e', 'a', 'c', 'd', 'b']
