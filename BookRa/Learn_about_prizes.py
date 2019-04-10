from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/Users/katepate/PycharmProjects/zae/chromedriver')
driver.implicitly_wait(5)
driver.get('https://vk.com/app3696901_71147356')

a = driver.find_element_by_id('quick_email')
time.sleep(5)
a.send_keys('katzxa@mail.ru')

b = driver.find_element_by_name('pass')
b.click()
b.send_keys('0505396291')
driver.implicitly_wait(5)

c = driver.find_element_by_id('quick_login_button')
c.click()

driver.implicitly_wait(10)

iframe = driver.find_elements_by_tag_name('iframe')[2]
driver.switch_to_frame(iframe)

driver.implicitly_wait(5)

elem = driver.find_element_by_xpath('/html/body/ui-view/default/div/div[2]/ui-view/lobby/div/div[3]/sidebar/div[2]/a/span')
elem.click()

driver.close()

