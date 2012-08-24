from optparse import OptionParser

p = OptionParser()

p.add_option('-d','--debug',action='store_true',
	dest = 'debug',help='Turn on debugging')

p.add_option('-s','--speed',action='store',
	type='int',dest = 'speed',
	help = 'Use a bigger number to go faster')

p.add_option('-u','--username',action='store',
	type='string',dest = 'user',
	help = 'Provide your username')

p.set_defaults(debug=False,speed=0)

options, args = p.parse_args()

if options.user is None:
	p.error('username is required')

print 'debug option is: %s' % options.debug
print 'speed option is: %s' % options.speed
print 'args are: %s' % args