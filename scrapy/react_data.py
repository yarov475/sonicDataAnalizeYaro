# from selenium import webdriver
#
# DRIVER_PATH = 'C:/Windows/chromedriver.exe'
# driver = webdriver.Chrome()
# driver.get('https://google.com')
# print('done driver')
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup

url = 'https://prozhito.org/notes?date=%221838-01-01%22'
# url = 'https://prozhito.org/note/442582'
# page = requests.get()
# soup = BeautifulSoup(page.content, 'html.parser')


options = Options()
options.headless = True
# options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options)
driver.get("https://prozhito.org/note/197636")

text = driver.find_element_by_class_name("notes-list__item clearfix scroll_row")
full = driver.page_source
print(text)
driver.quit()

# import scrapy
# import csv
# from selenium import webdriver
# print('fox')
#
#
# class AngularSpider(scrapy.Spider):
#     name = 'angular_spider'
#     start_urls = [
#         'http://www.example.com/?page=1',
#         'http://www.example.com/?page=2',
#     ]
#
#     # Initalize the webdriver
#     def __init__(self):
#         self.driver = webdriver.Firefox()
#
#     # Parse through each Start URLs
#     def start_requests(self):
#         for url in self.start_urls:
#             yield scrapy.Request(url=url, callback=self.parse)
#
#             # Parse function: Scrape the webpage and store it
#
#
#
#   # Parse function: Scrape the webpage and store it
#     def parse(self, response):
#         self.driver.get(response.url)
#         # Output filename
#         filename = "angular_data.csv"
#         with open(filename, 'a+') as f:
#             writer = csv.writer(f)
#             # Selector for all the names from the link with class 'ng-binding'
#             names = self.driver.find_elements_by_css_selector("a")
#             for name in names:
#                 title = name.text
#                 writer.writerow([title])
#         self.log('Saved file %s' % filename)
