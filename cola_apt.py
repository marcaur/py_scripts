#! /usr/bin/python3
from bs4 import BeautifulSoup as bs4

# SECTIONS NEEDED
# <div class="view-content"> ---- outer div containing the rows
# <div class="section--content"> --- contains: price,city,title
# <div class="section--content--top"> contains: title & price
# <div class="section--content--pricing"> contains: price & num of rooms
with open("cola2.html") as cola:
    soup = bs4(cola,'html.parser') # gets the full page

listInfo = soup.find_all('div',attrs={"class":"section--content--top"})

# for list in listInfo:
# name = listInfo.find('a').get_text() # both the title and city are <a> tags
i = 1
for list in listInfo:
    print("LISTING " + str(i) + ":" + str(list))
    print("=========================")
    i += 1

prices = soup.find_all('div', attrs={"class":"section--content--pricing"})
