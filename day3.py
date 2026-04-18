from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach",True)

#verfication properties

#1.title
"""
driver = Chrome(opts)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)
title = driver.title
print("title:",title)
driver.close()

"""

#2.current_url

"""
driver = Chrome(opts)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)
url = driver.current_url
print("url:",url)
driver.close()
"""

#3.page_source

"""
driver = Chrome(opts)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)
source = driver.page_source
print("source:",source)
driver.close()
"""

#selectors
  #1.id

driver = Chrome(opts)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)

#way-1
"""
search = driver.find_element("id","twotabsearchtextbox")
search.send_keys("mobiles")
sleep(3)

search_btn = driver.find_element("id","nav-search-submit-text")
search_btn.click()
"""
#way-2
driver.find_element("id","twotabsearchtextbox").send_keys("mobiles")
sleep(3)
driver.find_element("id","nav-search-submit-text").click()
