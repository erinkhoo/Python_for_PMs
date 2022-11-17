#Scraping dynamic data from a webpage using Selenium
from selenium import webdriver
import time


def get_drvr():
  #Chrome webdrivers to make scraping simpler
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-feature=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com")
  return driver


def clean_text(text):
  """Extract only the temp from text"""
  output = int(text.split(": ")[1])
  return output


def main():
  scrape = get_drvr()
  time.sleep(2.22)
  element = scrape.find_element(by="xpath",
                                value="/html/body/div[1]/div/h1[2]")
  return clean_text(element.text)


yo = main()
print(f'Temp is: {yo}')
