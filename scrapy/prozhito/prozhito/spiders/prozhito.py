import scrapy
import csv
from selenium import webdriver


class AngularSpider(scrapy.Spider):
    name = 'proshito'
    start_urls = [
        'https://prozhito.org/notes?date=%221800-01-01%22',
       # 'https://prozhito.org/notes?date=%221941-07-22%22',
        #'https://prozhito.org/note/169785',
    ]

    # Initalize the webdriver
    def __init__(self):
        self.driver = webdriver.Firefox()

    # Parse through each Start URLs
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

            # Parse function: Scrape the webpage and store it

    # Parse function: Scrape the webpage and store it
    def parse(self, response):
        self.driver.get(response.url)
        # Output filename
        # filename = "prozhito.csv"
        # with open(filename) as f:
            #writer = csv.writer(f)
            # Selector for all the names from the link with class 'ng-binding'
        #names = self.driver.find_elements_by_id("root")
        print(self.driver.page_source)
        #print(names)
            # for name in names:
            #
            #     writer.writerow(name)
        #self.log('Saved file %s' % filename)
