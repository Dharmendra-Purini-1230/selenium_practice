from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach",True)

driver = Chrome(opts)

#xpath by attribute
"""
driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
driver.find_element("xpath","(//input[@class = 'form-control'])[3]").send_keys("976596975")
"""
#1.xapth by text()

driver.get("https://demowebshop.tricentis.com/")
sleep(3)
driver.find_element("xpath","//a[text()= 'Register']").click()


"""
driver.get("https://demowebshop.tricentis.com/")
sleep(3)
driver.find_element("xpath","//a[text()='Books  ']").click() / spaces after books it throwserror
"""


