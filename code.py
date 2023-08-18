from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv 
import requests
import pandas as pd

start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("/Users/sanjik/Downloads/chromedriver-mac-x64/chromedriver")
brower.get(start_url)
time.sleep(10)

stars_data=[]
headers=["Name", "Distance", "Mass", "Radius"]

wiki = requests.get(START_URL)
soup = BeautifulSoup(wiki.text, "html.parser")
temp_list = []

for tr in soup.find("table").find_all("tr"):
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

for i in range(1, len(temp_list)):
    Name.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])

df = pd.DataFrame(
    list(zip(name, distance, mass, radius)),
    columns=["Star_name", "Distance", "Mass", "Radius"],
)
df.to_csv("data.csv")