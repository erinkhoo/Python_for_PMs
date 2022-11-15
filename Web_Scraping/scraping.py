#Scraping data from a webpage using Selenium
from selenium import webdriver

def get_driver():
  #Chrome webdrivers to make scraping simpler
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximised")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches",["enable-automation"])
  options.add_experimental_option("disable-blink-feature=AutomationControlled")

  driver = webdriver.Chrome(options)
  driver.get("https://automated.pythonanywhere.com")
  return driver

def main():
  scrape = get_driver()
  element = scrape.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
  return = element.text

print(main())