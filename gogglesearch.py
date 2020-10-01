# search on google then open top 5 site 
#firstly install google by "pip3 install google"
# import search by googlesearch
from googlesearch import *
#import webbrowser for access web by "webbrowser.open"
import webbrowser
query = input("Input your query:")
webbrowser.open_new_tab('https://www.google.com/search?q='+query)
#search on google 5 top tab open  
for i in search(query, tld="com", num=5 , stop = 5, pause = 2):
	webbrowser.open(i)
		

