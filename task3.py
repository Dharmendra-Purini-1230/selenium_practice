from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach",True)


x = int(input('enter x position:'))
y = int(input('enter y position:'))
driver = Chrome(opts)
driver.set_window_position(x,y)
driver.get("https://www.amazon.in/")