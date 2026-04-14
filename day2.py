#getting browser size:
    #get_window_size()

# getting browser position
    #get_window_position()

# getting browser size and positios
    #get_window_rect()

from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach",True)

#driver = Chrome(opts)
#driver.get("https://www.jiohotstar.com/")
#size = driver.get_window_size()
#print("size:",size)

#position = driver.get_window_size()
#print("position:",position)

#size_position = driver.get_window_rect()
#print("size_position:",size_position)


# set the browser size
     #set_window_size()

# set the browser position
    #set_window_position()

#set the browser size and position
    #set_window_rect()

driver = Chrome(opts)
driver.get("https://www.amazon.in/")
sleep(3)
#set_window_size()
#driver.set_window_size(500,400)

#set_window_position()
#driver.set_window_position(200,100)

#set_window_rect()
driver.set_window_rect(400,500,100,200)
driver.close()