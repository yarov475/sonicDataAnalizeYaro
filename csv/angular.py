import scrapy
import csv
from selenium import webdriver


class AngularSpider(scrapy.Spider):
    name = 'angular_spider'
    start_urls = [
        'https://www.example.com/?page=1',
        'https://www.example.com/?page=2',
    ]

    # Initalize the webdriver
    def __init__(self):
        self.driver = webdriver.Firefox()

    # Parse through each Start URLs
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

            # Parse function: Scrape the webpage and store it


def parse(self, response):
    self.driver.get(response.url)
    # Output filename
    filename = "angular_data.csv"
    with open(filename, 'a+') as f:
        writer = csv.writer(f)
        # Selector for all the names from the link with class 'ng-binding'
        names = self.driver.find_elements_by_css_selector("a.ng-binding")
        for name in names:
            title = name.text
            writer.writerow([title])
    self.log('Saved file %s' % filename)