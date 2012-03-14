#Define a procedure, add_page_to_index,
#that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

#It should update the index to include
#all of the word occurences found in the
#page content by adding the url to the
#word's associated url list.


index = []

#add_page_to_index(index,'fake.text',"This is a test")
#print index => [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']], ['test', ['fake.text']]]

def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
	keyword = content.split()
	for item in keyword:
		add_to_index(index,item,url)

add_page_to_index(index,'fake.text',"This is a test")
add_page_to_index(index,'real.text',"This is not a test")
print add_to_index

