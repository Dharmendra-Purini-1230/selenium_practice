from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach",True)

width = int(input('enter browser width:'))
height = int(input('enter browser height:'))
driver = Chrome(opts)
driver.set_window_size(width,height)
driver.get("https://www.amazon.in/")

