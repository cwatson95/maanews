##maanews

from bs4 import BeautifulSoup, SoupStrainer
import urllib2
import re
from firebase import firebase

# Connect to firebase
#firebase = firebase.FirebaseApplication('https://crackling-torch-4312.firebaseio.com/', None)
firebase = firebase.FirebaseApplication('https://fiery-torch-8096.firebaseio.com/', None)



# Make the soup, real quick
quMath_url = "http://www.maa.org/news/rss.xml"
page_html = urllib2.urlopen(quMath_url) 
soup = BeautifulSoup(page_html)
#soup = BeautifulSoup(page_html, "xml")



# Find article titles and print them
# titles = []
# for art in soup.find_all(attrs={"class": "field-content"}):
#      if '/news' in art:
#      	print art
     	#titles.append(art['title'])
#print titles
# titles = []
# for art in soup.find_all('a'):
# 	pair = (art.get('href'), art.text)
# 	if '/news/' in pair[0]:
# 		print art
titles = []
for art in soup.find_all('title'):
	#fullTitle = art.find_all
	#for x in art.find_all('script'):
	#titles.append(art['title'])
	# print art.string
	titles.append(art.string)

print titles	


# # Sift for article urls and print them
# urList=[]
# for urls in soup.find_all('link'):
# 	fullUrl = urls.find_all('a')[1]	#prints urls twice uses [1] to get first instance
# 	if fullUrl.has_attr('href'):
# 		urList.append(fullUrl['href'])

# 		print fullUrl['href']

# print fullUrl['href']


# #Find blurbs
# blurbs = []
# for para in soup.find_all('description'):
#     blurbs.append('description')

# #Put data onto firebase 
# for i in range(0, len(titles)):
#     result = firebase.post('/articles', {"blurb": blurbs[i], "url": urList[i], "title": titles[i]})	
#     print result






# In[ ]:
#Now for the blurb: turn each url into a soup 
#Possible starter method to scrape blurbs if the main page doesnt already have them

# for k in range(0, len(urList)):
# quMath_url = urList[2*k]
# page_html = urllib2.urlopen(quMath_url) 
# soup = BeautifulSoup(page_html)
# # Find article titles and print them
# #blurbs = []
# #for para in soup.find('p').getText():
#    #blurbs.append(para['data-listing-title'])
# #print soup.find('p').getText()
# result = firebase.post('/', soup.p)
# print result