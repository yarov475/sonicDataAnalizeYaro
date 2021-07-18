# import requests
# # from bs4 import BeautifulSoup
# #
# # page = requests.get('https://prozhito.org/note/200678')
# # soup = BeautifulSoup(page.content, 'html.parser')
# # print(soup.find_all('a'))



# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# listUrls = ["https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"]
# # browser = webdriver.PhantomJS('/usr/local/bin/phantomjs')
# browser = webdriver.Chrome("./chromedriver")
# urls=[]
#
# for url in listUrls:
#     browser.get(url)
#     soup = BeautifulSoup(browser.page_source,"html.parser")
#     results = soup.findAll('a',{'class':"mw-redirect"})
#     for result in results:
#         link = result["href"]
#         urls.append(link)
#     print(urls)
import scrapy
import csv
from selenium import webdriver