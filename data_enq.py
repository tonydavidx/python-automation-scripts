from selenium import webdriver
import time

driver = webdriver.Chrome()


def login():
    driver.get("http://192.168.8.1/html/home.html")
    driver.find_element_by_id("logout_span").click()
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_id("password").send_keys("asus6174")
    driver.find_element_by_id("pop_login").click()
    driver.find_element_by_id("sms").click()
    driver.find_element_by_id("message").click()
    driver.find_element_by_id("recipients_number").send_keys("123")
    driver.find_element_by_id("message_content").send_keys("stvenq")
    driver.find_element_by_id("pop_send").click()
    # driver.find_element_by_id("callCanvas").click()
    time.sleep(10)
    driver.quit()

login()

