from selenium import webdriver
from time import sleep
driver=webdriver.Chrome(executable_path="E:\chromedriver")
driver.get("https://www.instagram.com/")
sleep(4)
driver.find_element_by_xpath("//input[@name=\"username\"]")\
    .send_keys(" put your username")
driver.find_element_by_xpath("//input[@name=\"password\"]")\
    .send_keys("put your password ")
driver.find_element_by_xpath('//button[@type="submit"]')\
    .click()
sleep(4)
driver.get("https://www.instagram.com/_biswarup_bhattacharjee/")
following=driver.find_element_by_partial_link_text("following")
following.click()
sleep(5)
for i in range (20):
    driver.find_element_by_xpath('//button[text()="Following"]')\
        .click()
    driver.find_element_by_xpath('//button[text()="Unfollow"]')\
        .click()
    sleep(2)        