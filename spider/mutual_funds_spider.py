# coding=utf-8
import
import logging

from base.model.document import Stock
from helper.args_parser import stock_spider_parser

from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions

url="http://fundlibrary.com/tools/nav_lookup.asp?"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.implicitly_wait(1)
browser.get(url)

for year in range (2010, 2018):
    b.find_element_by_xpath("//select[@name='txtYear']/option[text()='%s']" % year).click()
    for month in range (1, 12):
        b.find_element_by_xpath("//select[@name='txtMonth']/option[text()='%s']" % month ).click()
        for day in range (1, 31):
            b.find_element_by_xpath("//select[@name='txtDay']/option[text()='%s']" % day).click()


            element = browser.findElement(By.id("txtFundName"))
            element.send_keys("TD U.S. Blue Chip Equity Fund - Investor Series")
            button = driver.find_elements_by_xpath("//input[@name='btnName' and @src='/gfx/btnSearch.jpg']")[0]
            button.click()
FLFUNDNAME

old_value = browser.find_element_by_id('thing-on-old-page').text
browser.find_element_by_link_text('my link').click()
WebDriverWait(browser, 3).until(
    expected_conditions.text_to_be_present_in_element(
        (By.ID, 'thing-on-new-page'),
        'expected new text'
    )
)


            soup = BeautifulSoup(html_doc, 'html.parser')


class StockSpider(object):
    def __init__(self, code, start="2008-01-01", end="2018-01-01"):
        self.code = code
        self.start = start
        self.end = end

    def crawl(self):
        stock_frame = ts.get_k_data(code=self.code, start=self.start, end=self.end, retry_count=30)
        for index in stock_frame.index:
            stock_series = stock_frame.loc[index]
            stock_dict = stock_series.to_dict()
            stock = Stock(**stock_dict)
            stock.save_if_need()
        logging.warning("Finish crawling code: {}, items count: {}".format(self.code, stock_frame.shape[0]))


def main(args):
    codes = args.codes
    # codes = ['sh']
    for _code in codes:
        StockSpider(_code, args.start, args.end).crawl()


if __name__ == '__main__':
    main(stock_spider_parser.parse_args())
