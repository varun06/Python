def get_next_target(page):
    start_link = page.find('<a href=')

    #Insert your code here
    if(start_link == -1):
    	url = None
        end_quote = 0
        return url,end_quote
    else:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote

print get_next_target('This is the page <a href = "http:google.com">') 