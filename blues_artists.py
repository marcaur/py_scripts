# gather the names of all blues rock guitarists on wiki page
# sort by last name and create chart with frequency of names
import csv
from bs4 import BeautifulSoup
import requests


urls = ["https://en.wikipedia.org/wiki/Category:Blues_rock_musicians"]
rows = []
def website_scrape(url):
    page = requests.get(url)
    page_content = page.content
    # create the object
    soup = BeautifulSoup(page_content,"html.parser")
    content = soup.find("div", class_="mw-category")
    # creates a list element of all groups
    all_groupings = content.find_all("div", class_="mw-category-group")
    for group in all_groupings:
        lastName = group.find("h3").get_text()
        nameSection = group.find("ul")
        artistList = nameSection.find_all("li")
        # get the row of info for csv file
        for artist in artistList:
            name = artist.text
            name_Tag = artist.find("a", href=True)
            name_Link = name_Tag["href"]
            letter_Name = lastName
            # row of data created through each loop
            row = {
                "Category":letter_Name,
                "Name":name,
                "Link":name_Link
                }
            rows.append(row)

for url in urls:
    website_scrape(url)

# CREATING THE CSV FILE
with open("blues_guitar_artists.csv","w+") as csv_file:
    fieldNames = ["Category","Name","Link"]
    writer = csv.DictWriter(csv_file,fieldnames=fieldNames)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
