def get_page(url):
	try:
		import urllib
		return urllib.urlopen(url).read()
	except Exception, e:
		return " "
		raise e

print get_page('www.google.com')