from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach",True)


#locator
  #5.link text
"""
driver = Chrome(opts)
driver.get("https://www.instagram.com/accounts/login/?hl=en")
sleep(3)
driver.find_element("link text","Forgot password?").click()
"""

#6.partial link text

"""
driver = Chrome(opts)
driver.get("https://www.instagram.com/accounts/login/?hl=en")
sleep(3)
driver.find_element("partial link text","new").click()
"""

#7.css selector

driver = Chrome(opts)
driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
#driver.find_element("css selector","input[value = 'male'][value = female]").click()

driver.find_element("css selector","input[value = 'female']").click()