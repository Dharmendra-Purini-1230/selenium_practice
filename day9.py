from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach",True)

driver = Chrome(opts)

"""
driver.get("https://www.instagram.com/?hl=en")
sleep(3)
driver.find_element("xpath","//input[contains(@id,'_R_')]").send_keys("dharma@gmail.com")
"""

#completely dyanamic
 #1.forward trversing
 #2.backward traversing

"""
driver.get("https://www.amazon.in/")
sleep(3)
driver.find_element("id","twotabsearchtextbox").send_keys("iphone")
sleep(3)
driver.find_element("id","nav-search-submit-button").click()
sleep(3)
price = driver.find_element("xpath","//span[text()='iPhone Air 256 GB: Thinnest iPhone Ever, 16.63 cm (6.5″) Display with Promotion up to 120Hz, Powerful A19 Pro Chip, Center Stage Front Camera, All-Day Battery Life; Space Black']/../../../..//span[@class='a-price-whole']")
print(price.text)
sleep(3)
rating = driver.find_element("xpath","//span[text()='iPhone Air 256 GB: Thinnest iPhone Ever, 16.63 cm (6.5″) Display with Promotion up to 120Hz, Powerful A19 Pro Chip, Center Stage Front Camera, All-Day Battery Life; Space Black']/../../../..//span[@class='a-size-small a-color-base']")
print(rating.text)
sleep(3)
"""


driver.get("https://www.flipkart.com/")
sleep(3)
driver.maximize_window()
sleep(3)
driver.find_element("xpath","//span[@class = 'b3wTlE']").click()
sleep(3)
driver.find_element("xpath","//input[@type = 'text']").send_keys("iphone")
sleep(3)
driver.find_element("xpath","//button[@class = 'XFwMiH']").click()
sleep(3)
price = driver.find_element("xpath","//div[text()='Apple iPhone 16 (Black, 128 GB)']/../..//div[@class='hZ3P6w DeU9vF']")
print(price.text)