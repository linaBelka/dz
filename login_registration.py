#2

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("http://practice.automationtesting.in/")
# driver.maximize_window()
# my_account=driver.find_element_by_link_text('My Account').click()
# mail=driver.find_element_by_id('reg_email')
# mail.send_keys("lina@mail.ru")
# pasword=driver.find_element_by_id('reg_password')
# pasword.send_keys("LinaBelka123!//")
# sf=driver.find_element_by_css_selector('[class="woocommerce-Button button"]').click()
# btn=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[value="Register"]'))).click()

#3
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("http://practice.automationtesting.in/")
# driver.maximize_window()
# my_account=driver.find_element_by_link_text('My Account').click()
# Username =driver.find_element_by_id('username')
# Username.send_keys("lina@mail.ru")
# pasword=driver.find_element_by_id('password')
# pasword.send_keys("LinaBelka123!//")
# login=driver.find_element_by_css_selector('[value="Login"]').click()
# Log = WebDriverWait(driver, 5).until( EC.text_to_be_present_in_element ((By.CSS_SELECTOR, '[class="woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--customer-logout"]'), "Logout"))
#
