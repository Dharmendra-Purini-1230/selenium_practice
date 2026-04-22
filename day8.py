from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach",True)

driver = Chrome(opts)

#2.contains
  #1.xpath by contains() and text()
"""
driver.get("https://demowebshop.tricentis.com/")
sleep(3)
driver.find_element("xpath","(//a[contains(text(),'Books')])[3]").click()
"""
 
 #2.xpath by contains() and atrribute

"""
driver.get("https://demowebshop.tricentis.com/")
sleep(3)
driver.find_element("xpath","//a[contains(@class,'ico-login')]").click()
"""

"""
driver.get("https://www.instagram.com/accounts/login/?hl=en")
sleep(3)
driver.find_element("xpath","(//input[contains(@class,'x1i10hfl xggy1nq')])[1]").send_keys("dharma@gmail.com")
"""

"""
driver.get("https://www.amazon.in/")
sleep(3)
driver.find_element("id","twotabsearchtextbox").send_keys("niva sport volleyball")
sleep(3)
driver.find_element("id","nav-search-submit-button").click()
"""

driver.get("https://www.flipkart.com/")
sleep(3)
driver.maximize_window()
sleep(3)
driver.find_element("xpath","//span[@class = 'b3wTlE']").click()
sleep(3)
driver.find_element("xpath","//input[@type = 'text']").send_keys("volleyball")
sleep(3)
driver.find_element("xpath","//button[@class = 'XFwMiH']").click()
