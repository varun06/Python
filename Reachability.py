#Reachability

#Single Gold Star

#Define a procedure, reachable(graph, node), that takes as input a graph and a
#starting node, and returns a list of all the nodes in the graph that can be
#reached by following zero or more edges starting from node.  The input graph is
#represented as a Dictionary where each node in the graph is a key in the
#Dictionary, and the value associated with a key is a list of the nodes that the
#key node is connected to.  The nodes in the returned list may appear in any
#order, but should not contain any duplicates.

def reachable(graph,node):
	return reachablity(graph,node,seen = None)
	pass

def reachablity(graph,node,seen = None):
	seen = seen or []
	seen.append(node)
	reached = set(node)
	adjacent = graph.get(node)
	
	if adjacent:
		reached.update(adjacent)
		for subnode in adjacent:
			if subnode in adjacent:
				if subnode not in seen:
					reached.update(reachablity(graph,subnode,seen))
	Final_result = list(reached)
	return Final_result

#For example,

graph = {'a': ['b', 'c'], 'b': ['a', 'c'], 'c': ['b', 'd'], 'd': ['a'], 'e': ['a']}

print reachable(graph, 'a')
#>>> ['a', 'c', 'd', 'b']

print reachable(graph, 'd')
#>>> ['d', 'a', 'c', 'b']

print reachable(graph, 'e')
#>>> ['e', 'a', 'c', 'd', 'b']
