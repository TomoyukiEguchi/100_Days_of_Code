from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/tomoyukieguchi/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# number_of_articles = driver.find_element_by_css_selector("#articlecount a")
# # print(number_of_articles.text)
#
# all_portals = driver.find_element_by_link_text("All portals")
# # all_portals.click()
#
# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element_by_name("fName")
f_name.send_keys("python")
l_name = driver.find_element_by_name("lName")
l_name.send_keys("python")
email_address = driver.find_element_by_name("email")
email_address.send_keys("python@python.com")

submit = driver.find_element_by_css_selector("form button")
submit.click()