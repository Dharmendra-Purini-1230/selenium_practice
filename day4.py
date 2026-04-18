from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
opts = ChromeOptions()
opts.add_experimental_option("detach",True)

#selectors
  #2.name
"""
driver = Chrome(opts)
driver.get("https://jntuaresults.ac.in/view-results?resultSetId=41a5708d-0f1f-4def-99c3-07ddf3f32f2b")
sleep(3)
driver.find_element("name","hallTicketNumber").send_keys("214N1A0550")
"""

'''
driver = Chrome(opts)
driver.get("https://www.facebook.com/login.php?next=https%3A%2F%2Fwww.facebook.com%2Foidc%2F%3Fapp_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignupviafb%252F%26response_type%3Dcode%26scope%3Dopenid%2Bemail%2Bprofile%2Blinking%26state%3DATqIs5EetKgWMRw3TxbzGEEp4xJnDY5ZB6t1JXxU-Z6q4ekK1gp8zwEd329d5qxje1FgizKVq89oCZF9nxLBP7YWn_EciQYCIxJi9r1KAoeu4F4ZKx9tyNu2n7S6r0mje3uQC6eZrpk4UNIr7XaVpO1Creiur7tQf0wCtzwnktR6ZY_mXTBaScgtqNg10u3adWF4IkOrSk05I-oLuNxyGRWQAdEwomw5magpe66-9C6Idnob903ohg_LS6UmpjoPmLTMRG_whHjr3ZrypIdeaH4mKQ")
sleep(3)
driver.find_element("name","email").send_keys("dharma@gmail.com")
sleep(3)
driver.find_element("name","pass").send_keys("1230")
'''
"""
driver = Chrome(opts)
driver.get("https://student.qspiders.com/login")
sleep(3)
driver.find_element("class","px-3.h-9.max-w-full.focus:ring.focus:outline-none.dark:placeholder-gray-400.w-full.h-4.border-0.border-white.pt-0.dark:bg-gray-800.rounded.pr-10").send_keys("9640581310")
"""
#locator
  #3.class
'''
driver = Chrome(opts)
driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
driver.find_element("class name","form-control").send_keys("dharma")
#driver.find_element(By.CLASS_NAME,"form-control").send_keys("dharma")
sleep(3)
driver.find_element("class name","form-control").send_keys("dharma@gmail.com")
'''


#find_elements()

#4.tag name


"""
driver = Chrome(opts)
driver.get("https://www.amazon.in/")
sleep(3)
a = driver.find_elements("tag name","li")
print(a)
print(len(a))
"""










