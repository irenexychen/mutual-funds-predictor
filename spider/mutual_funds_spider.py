# coding=utf-8
from base.model.document import Stock
from helper.args_parser import stock_spider_parser
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions


class StockSpider(object):
    def __init__(self, code, start="2008-01-01", end="2018-01-01"):
        self.code = code
        self.start = start
        self.end = end

    def crawl(self):
        url="http://fundlibrary.com/tools/nav_lookup.asp?"

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        browser = webdriver.Chrome(chrome_options=chrome_options)
        browser.implicitly_wait(1)
        browser.get(url)
        try:
            wait = WebDriverWait(browser, 2)
            wait.until(expected_conditions.element_to_be_clickable((By.ID, 'btnSearch')))
          
            for year in range (2017, 2018):
                browser.find_element_by_xpath("//select[@name='txtYear']/option[text()='%s']" % year).click()
                for month in range (1, 3):
                    browser.find_element_by_xpath("//select[@name='txtMonth']/option[@value='%s']" % month ).click()
                    for day in range (1, 3):
                        browser.find_element_by_xpath("//select[@name='txtDay']/option[@value='%s']" % day).click()
                        print(month)
                        print(day)
                        #driver.findElement(By.xpath("//input[@id='invoice_supplier_id'])).sendKeys("your value");
                        elementFund = browser.find_elements_by_name("txtFundName")[1]

                        # Hack, the second
                        #elementFund = elementFund.find_element_by_xpath("following-sibling::td")
                        #elementFund = browser.find_element_by_name("txtFundName")
                        elementFund.send_keys("TD U.S. Blue Chip Equity Fund - Investor Series")
                        #elementFund.send_keys("TD U.S. Blue Chip Equity Fund - Investor Series")
                        print(elementFund.get_attribute('value'))
                       
                        button = browser.find_element_by_name('btnName')
                        #button = browser.find_element_by_xpath("(//input[@name='btnName'])[2]")
                        #button = browser.find_element_by_xpath("//input[@name='btnName' and @src='/gfx/btnSearch.jpg']")[0]
      
                        button.click()

                        wait = WebDriverWait(browser, 2)
                        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME , 'FLFUNDNAME')))
          
                        #fundElement = browser.find_element_by_class_name('FLFUNDNAME')
                        #print(fundElement.text)
                        
                        fund = browser.find_elements_by_class_name('FLROW')
                        #dateElement = fundElement.find_element((By.XPATH,"following-sibling::td[@class='FLROW']"))
                        #priceElement = dateElement.find_element((By.XPATH,"following-sibling::td[@class='FLROW']"))
                        print(fund[0].text)
                        print(fund[1].text)
        finally:
            browser.quit()

        
                    #old_value = browser.find_elements_by_class_name('FLFUNDNAME').text
                    
                    #browser.find_element_by_link_text('popUpWindow2').click()


                    #WebDriverWait(browser, 3).until(expected_conditions.text_to_be_present_in_element((By.ID, 'thing-on-new-page'),'expected new text'))


            #soup = BeautifulSoup(html_doc, 'html.parser')

      #stock = Stock(**stock_dict)
      #      stock.save_if_need()
      #  logging.warning("Finish crawling code: {}, items count: {}".format(self.code, stock_frame.shape[0]))


def main(args):
    codes = args.codes
    for _code in codes:
        StockSpider(_code, args.start, args.end).crawl()


if __name__ == '__main__':
    main(stock_spider_parser.parse_args())