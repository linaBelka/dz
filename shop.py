# 4/4
# import time
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
# shop=driver.find_element_by_link_text("Shop").click()
# html5=driver.find_element_by_css_selector('[title="Mastering HTML5 Forms"]').click()
# text = WebDriverWait(driver, 5).until( EC.text_to_be_present_in_element ((By.CSS_SELECTOR, '[class="product_title entry-title"]'), "HTML5 Forms"))

# 4/5
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
# shop=driver.find_element_by_link_text("Shop").click()
# #
#
# html=driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/product-category/html/"]').click()
# books = driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
# if len(books) == 3:
#     print("3")
# else:
#     print( str(len(books)));


#4/6
# from selenium.webdriver.support.select import Select
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
# shop=driver.find_element_by_link_text("Shop").click()
# sort = driver.find_element_by_name("orderby")
# sort = sort.get_attribute("value")
# print("value of sort celekt: ", sort )
# if sort=='menu_order':
#     print("Default sorting")
# else:
#     print("другое")
# sort = driver.find_element_by_name("orderby")
# select=Select(sort)
# select.select_by_index("4")
# sort = driver.find_element_by_name("orderby")
# sort = sort.get_attribute("value")
# print("value of sort celekt: ", sort )
# if sort=='price':
#     print("Sort by price: low to high")
# else:
#     print("другое")

# 4/7
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
# shop=driver.find_element_by_link_text("Shop").click()
# android=driver.find_element_by_css_selector('[alt="Android Quick Start Guide"]').click()
# old_price=driver.find_element_by_css_selector('.price>del>span')
# old_price_text=old_price.text
# new_price=driver.find_element_by_css_selector('.price>ins>span')
# new_price_text=new_price.text
# assert old_price_text=='₹600.00'
# assert new_price_text=='₹450.00'
# book=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.images'))).click()
# book_close=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.pp_close'))).click()

#4/8
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("http://practice.automationtesting.in/")
# driver.maximize_window()
# shop=driver.find_element_by_link_text("Shop").click()
# html_development=driver.find_element_by_css_selector('[data-product_id="182"]').click()
# time.sleep(5)
# basket=driver.find_element_by_class_name('cartcontents')
# basket_text=basket.text
# price=driver.find_element_by_css_selector('.wpmenucart-contents>span:nth-child(3)')
# price_text=price.text
# assert basket_text=='1 Item'
# assert price_text=='₹180.00'
# basket=driver.find_element_by_class_name('cartcontents').click()
# Subtotal = WebDriverWait(driver, 5).until( EC.text_to_be_present_in_element ((By.CSS_SELECTOR, '[class="cart-subtotal"]>td>span:nth-child(1)'),'180.00'))
# Total=WebDriverWait(driver, 5).until( EC.text_to_be_present_in_element ((By.CSS_SELECTOR, '[class="order-total"]>td'),'189.00'))


#4/9
# import time
#
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.get("http://practice.automationtesting.in/")
# driver.maximize_window()
# shop=driver.find_element_by_link_text("Shop").click()
# driver.execute_script("window.scrollBy(0, 300);")
# HTML5_WebApp_Development=driver.find_element_by_css_selector('[data-product_id="182"]').click()
# time.sleep(3)
# driver.execute_script("window.scrollBy(0, 600);")
# JS_Data_Structures_Algorithm=driver.find_element_by_css_selector('[data-product_id="180"]').click()
# basket=driver.find_element_by_class_name('cartcontents').click()
# time.sleep(3)
# delete=driver.find_element_by_css_selector('[data-product_id="182"]').click()
# time.sleep(3)
# undo=driver.find_element_by_link_text('Undo?').click()
# quantily=driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
# quantily.clear()
# quantily.send_keys("3")
# update_basket=driver.find_element_by_css_selector('[name="update_cart"]').click()
# quantily=driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
# quantily_value=quantily.get_attribute("value")
# assert quantily_value=="3"
# time.sleep(2)
# coupon=driver.find_element_by_css_selector('[value="Apply Coupon"]')
# coupon.click()
# time.sleep(3)
# enter_coupon_code=driver.find_element_by_css_selector('[class="woocommerce-error"]')
# enter_coupon_code_text=enter_coupon_code.text
# assert enter_coupon_code_text=='Please enter a coupon code.'


# 4/10
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("http://practice.automationtesting.in/")
driver.maximize_window()
shop=driver.find_element_by_link_text("Shop").click()
driver.execute_script("window.scrollBy(0, 300);")
HTML5_WebApp_Development=driver.find_element_by_css_selector('[data-product_id="182"]').click()
time.sleep(2)
basket=driver.find_element_by_class_name('cartcontents').click()
PROCEED_TO_CHECKOUT=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="checkout-button button alt wc-forward"]'))).click()
first_name=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[name="billing_first_name"]')))
First_Name=driver.find_element_by_css_selector('[name="billing_first_name"]')
First_Name.send_keys('lina@mail')
Last_Name=driver.find_element_by_css_selector('[name="billing_last_name"]')
Last_Name.send_keys('belka')
mail=driver.find_element_by_css_selector('[type="email"]:nth-child(2)')
mail.send_keys('lina@mail.com')
Phone=driver.find_element_by_css_selector('[id="billing_phone"]')
Phone.send_keys('89999999999')
county=driver.find_element_by_css_selector('[role="presentation"]')
county.click()
county=driver.find_element_by_css_selector('[id="s2id_autogen1_search"]')
county.send_keys('roma')
romania=driver.find_element_by_css_selector('[class="select2-match"]').click()
address= driver.find_element_by_css_selector('[name="billing_address_1"]')
address.send_keys('lenina')
toun=driver.find_element_by_css_selector('[name="billing_city"]')
toun.send_keys('Izhevsk')
postcode=driver.find_element_by_css_selector('[name="billing_postcode"]')
postcode.send_keys('123456')
driver.execute_script("window.scrollBy(0, 600);")
State_County=driver.find_element_by_css_selector('[name="billing_state"]')
State_County.send_keys('russia')
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
Check_Payments=driver.find_element_by_css_selector('[id="payment_method_cheque"]').click()
place_order=driver.find_element_by_css_selector('[value="Place order"]').click()
Thank_you=WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'[class="woocommerce-thankyou-order-received"]'),"Thank you. Your order has been received."))
Payment_Method=WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[class="method"]'), "Check Payments"))


