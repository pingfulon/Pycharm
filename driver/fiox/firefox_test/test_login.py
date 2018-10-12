from selenium import webdriver
from time import sleep
def test_1(func):
    def test(*args, **kwargs):
        driver = webdriver.Firefox()
        driver.get('https://siotdev.lenovo.com.cn')
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[1]/div/a").click()
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/div/p[3]/a").click()
        sleep(2)
        driver.find_element_by_xpath("//input[@id='tuser']").send_keys("2583036030@qq.com")
        driver.find_element_by_xpath("//*[@id='tpass']").send_keys("@12345678")
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/form[1]/div/div[2]/div[4]/div[1]/input").click()
        sleep(2)
        return func(*args, **kwargs)
    return test
test_1()