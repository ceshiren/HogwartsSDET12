from appium import webdriver
from selenium.webdriver.common.by import By


def test_xueqiu():
    caps = {}
    caps["platformName"] = "Android"
    caps["deviceName"] = "127.0.0.1:7555"
    caps["appPackage"] = "com.xueqiu.android"
    caps["appActivity"] = ".view.WelcomeActivityAlias"
    caps['noReset'] = "true"
    caps['chromedriverExecutable']="D:/develop/chromedriver/2.20.exe"
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, "//*[@text='交易']").click()
    webview = driver.contexts[-1]
    driver.switch_to.context(webview)
    performance = driver.execute_script("return window.performance.timing")
    print(performance['domComplete'] - performance['responseStart'])
