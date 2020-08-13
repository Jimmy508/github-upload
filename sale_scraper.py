from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests
import csv

my_url = "https://www.newegg.com/Gadgets-Wearables/Category/ID-6"

#opening up the connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()


#html parsing
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll("div", {"class":"item-container"})

#TESTING TESTING TESTING#
