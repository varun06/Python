class Instrument(object):
	def __init__(self, name):
		self.name = name
	def has_strings(self):
		return True

class StringInstrument(Instrument):
	def __init__(self, name, count):
		# super(StringInstrument,self).__init__(name)
		Instrument.__init__(self, name)
		self.count = count

class Guitar(StringInstrument):
	def __init__(self):
		# super(Guitar, self).__init__('guitar', 6)
		StringInstrument.__init__(self, 'guitar', 6)

# class PercussionInstrument(Instrument):
# 	def has_strings(self):
# 		return False

# guitar = Instrument('guitar')
# drums = PercussionInstrument('drums')

guitar = Guitar()

# print 'Guitar has strings: {0}'.format(guitar.has_strings())
print 'Guitar name: {0}'.format(guitar.name)
# print 'Drums have strings: {0}'.format(drums.has_strings())
# print 'Drums name: {0}'.format(drums.name)
print 'Guitar count: {0}'.format(guitar.count)