import itertools

CLAIM = '{0} is the #{1} {2} language'

def best(type, *args):
	langs = []
	for i, arg in enumerate(args):
		langs.append(CLAIM.format(arg, i+1, type))
		return langs

def best_functional(*args):
	return best('functional', *args)

def best_oo(*args):
	return best('OO',*args)
	
for claim in itertools.chain(best_functional('Haskell', 'Earlang'), [''],
		best_oo('Objective-C', 'Java')):
	print claim