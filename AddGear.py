print("hello World")
from selenium import webdriver

driver = webdriver.Chrome()
loadpage = driver.get("https://hiking-gear.herokuapp.com/addgear")
name = loadpage.find_element_by_name("name")


name.send_keys("Rain Coat")

brand = loadpage.find_element_by_name("brand")
brand.send_keys("REI")

driver.implicitly_wait(5)

driver.quit()