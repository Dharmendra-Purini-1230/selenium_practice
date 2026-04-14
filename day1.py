
#from selenium.webdriver import Chrome

#c = Chrome()

#from selenium import webdriver

#driver = webdriver.Chrome()

#from selenium.webdriver import Chrome,ChromeOptions
#opts = ChromeOptions()
#opts.add_experimental_option("detach",True)
#c = Chrome(opts)

#from selenium.webdriver import Chrome,ChromeOptions
#opts = ChromeOptions()
#opts.add_experimental_option("detach",True)
#c = Chrome(opts)
#c.close()

#from selenium.webdriver import Chrome,ChromeOptions
#from time import sleep
#opts = ChromeOptions()
#opts.add_experimental_option("detach", True)
#c = Chrome(opts)  #open the browser
#sleep(3)
#c.close()  # it close the current tab

#from selenium.webdriver import Chrome,ChromeOptions
#from time import sleep
#pts = ChromeOptions()
#opts.add_experimental_option("detach",True)
#c = Chrome(opts)
#sleep(3)
#c.close()
#c.quit()

#from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
#opts = ChromeOptions()
#opts.add_experimental_option("detach",True)
#c = Chrome(opts)
#c.get("www.amajon.in")#invalid argument excepion
#c.get("https://www.amazon.in/")
#sleep(10)
#c.close()


#Lanching of amazon , flipkart,myntra based on the user input:

#from selenium.webdriver import Chrome,ChromeOptions
#from time import sleep
#opts = ChromeOptions()
#opts.add_experimental_option("detach",True)
#print("applications:\n1.amazon\n2.flipkart\n3.myntra")
#app = int(input("enter your choice:"))
#if app == 1:
 #   c = Chrome(opts)
    #c.get("https://www.amazon.in/")
#elif app == 2:
   #c = Chrome(opts)
    #c.get("https://www.flipkart.com/")
#elif app == 3:
    #c = Chrome(opts)
    #c.get("https://www.myntra.com/")
#else:
    #print("invalid choice")


#Broser commands
# maximize_window()

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach",True)



#driver = Chrome(opts)
#driver.get("https://www.amazon.in/")
#sleep(4)
#driver.maximize_window()
#driver.close()


#minimize_window():

#driver = Chrome(opts)
#driver.get("https://www.amazon.in/")
#sleep(3)
#driver.minimize_window()
#sleep(3)
#driver.maximize_window()

#fullscreen_window():

#driver = Chrome(opts)
#c
#sleep(3)
#driver.fullscreen_window()

#back():

#driver = Chrome(opts)
#driver.get("https://www.amazon.in/")
#sleep(3)
#driver.get("https://www.flipkart.com/")
#sleep(3)
#driver.back()

# forward():

#driver = Chrome(opts)
#driver.get("https://www.amazon.in/")
#sleep(3)
#driver.get("https://www.flipkart.com/")
#sleep(3)
#driver.back()
#sleep(3)
#driver.forward()

# refresh()

driver = Chrome(opts)
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)
driver.refresh()

