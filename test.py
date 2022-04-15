from selenium import webdriver

email = "dd_test_1@outlook.com"
password = "}krK,gdC6"


url = "https://vsmonitor.com"
driver = webdriver.Chrome("C:\webdriver1\chromedriver.exe")
driver.get(url)
driver.implicitly_wait(15)


driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_id("login-button").click()

