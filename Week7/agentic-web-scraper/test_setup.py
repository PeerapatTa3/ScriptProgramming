from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://books.toscrape.com/")
print("Title:", driver.title)
driver.quit()
