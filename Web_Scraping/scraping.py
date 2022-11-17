#Scraping data from a webpage using Selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_drvr():
  #Chrome webdrivers to make scraping simpler
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-feature=AutomationControlled")

  driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
  driver.get("https://automated.pythonanywhere.com")
  return driver


def main():
  scrape = get_drvr()
  element = scrape.find_element(by="xpath",
                                value="/html/body/div[1]/div/h1[1]")
  return element.text


print(main())
