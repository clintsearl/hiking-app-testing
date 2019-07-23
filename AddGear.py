print("hello World")
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
loadpage = driver.get("https://hiking-gear.herokuapp.com/addgear")
name = driver.find_element_by_name("name")

driver.implicitly_wait(5)

name.click()
name.send_keys("Rain Coat")

brand = driver.find_element_by_name("brand")
brand.send_keys("REI")

catagory = driver.find_element_by_tag_name("select")
catagory.click()
# catagory.find_element("option")
# allOptions = catagory.find_elements_by_tag_name("option")
# for option in allOptions:
    # print option.get_attribute("value")
choose = Select(driver.find_element_by_tag_name("select"))
choose.select_by_visible_text("Clothing")

units = driver.find
driver.quit()