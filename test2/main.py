from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# search Digikala
driver.get("https://www.digikala.com")


# find Log in
driver.find_element_by_xpath("// a[contains(text(),\'ورود به حساب کاربری')]").click()
sleep(1)



# find Edit text to write username
el = driver.find_element('name','login[email_phone]')
el.send_keys("09012366440")
sleep(2)



# submit
driver.find_element_by_xpath('//button[normalize-space()="ورود به دیجی‌کالا"]').click()
sleep(2)



# Enter password
el = driver.find_element('name','login[password]')
el.send_keys("DotinDotin1234")
sleep(2)



# submit
submit2 = driver.find_element_by_xpath('//button[normalize-space()="ادامه"]')
submit2.click()


# show profile
elements = driver.find_element_by_xpath("//*[@class='c-header__btn-profile js-dropdown-toggle']")
elements.click()
sleep(5)