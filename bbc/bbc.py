from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os

myUrl = '''https://www.bbc.com/news'''
print(myUrl)


# Opening up connection and grabbing the page
uClient = uReq(myUrl)

# Reading and saving the page
page_html = uClient.read()

# Closing the connection
uClient.close()

# Saving and parsing the data
page_soup = soup(page_html, "html.parser")


# Parsing to get all objects of same class
newses = page_soup.findAll(
    "h3")

print(len(newses))

num = 0
while(True):
    if(os.path.exists("news"+str(num)) == False):
        os.mkdir("news" + str(num))
        os.chdir("news" + str(num))
        break
    num += 1

num = 0
filename = "file"

for news in newses:
    f = open(filename+str(num) + ".txt", "w")
    f.write(news.text)
    f.close()
    num += 1
