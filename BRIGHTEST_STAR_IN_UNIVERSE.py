### imports ###
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import csv
### giving the path to fetch ###
BRIGHT_STAR_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome("C:/Users/DELL/Desktop/Python_Class/CLASS 127 WEB SCREAPPING _1 HOMWWORK/chromedriver")
page = requests.get(BRIGHT_STAR_URL)
print(page)
### location to frind the data ###
soup=BeautifulSoup(page.text,'html.parser')

star_table=soup.find('table')

temp_list=[]

table_rows=star_table.find_all('tr')
### loop ###
for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)
### variables ###
Star_names = []
Distance =[]
Mass = []
Radius =[]
### loop ###
for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])

### csv giving ###
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)
### creating the csv ###
df2.to_csv('BRIGHTNING_STARS---gagan---.csv')



##################################
##################################
##################################
                                  ##
\             @@@@@@              ###
\          @@@@@@@@@@@            ######
\        @@@         @@@          ############
\        @@@                      #################
\       @@@                       #######################             #####
\       @@@    @@@@@@@@@          #############################   #   #######
\       @@@    @@@   @@@          #######################             #####
\        @@@   @@@   @@@          #################
\        @@@@@@@@@   @@@          ############
\          @@@@@      @@          ######
                                  ###
##################################
##################################
##################################
signed by:- 26/12/2021
௹Å௹Å₦