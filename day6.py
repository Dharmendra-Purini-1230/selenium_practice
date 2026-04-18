from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach",True)

#8.xpath
   #1.apsulute xpath
   
"""
driver = Chrome(opts)
driver.get("https://demowebshop.tricentis.com/register")
#driver.get("/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a")
driver.get("https://demowebshop.tricentis.com/")
sleep(3)
#driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[1]/div[1]/input").click()
driver.find_element("xpath","/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a").click()
sleep(3)
driver.close()
"""

   #2.Relative xpath
       #1.basic
 
driver = Chrome(opts)
driver.get("https://demowebshop.tricentis.com/register")
           


