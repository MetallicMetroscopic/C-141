from bs4 import BeautifulSoup
import pandas as pd
import time
import requests

src_website_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
chrome = requests.get(src_website_url)

time.sleep(10)

stars_data = []
name = []
distance = []
mass = []
radius = []


soup = BeautifulSoup(chrome.text, "html.parser")

for tr_tags in soup.find("table").find("tbody").find_all("tr"):
    td_tags = tr_tags.find_all("td")
    temp_list = []

    for td_tag in td_tags:
        td_tag = td_tag.text.strip()
        temp_list.append(td_tag)

    stars_data.append(temp_list)

for i in range(1,len(stars_data)):
    name.append(stars_data[i][1])
    distance.append(stars_data[i][3])
    mass.append(stars_data[i][5])
    radius.append(stars_data[i][6])

stars_data_dictionary = {
    "Star Name": name,
    "Distance": distance,
    "Mass": mass,
    "Radius": radius,
}

stars_table = pd.DataFrame(stars_data_dictionary)
stars_table.to_csv("stars_table.csv", index=True, index_label="id")
