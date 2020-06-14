import logging
import subprocess
from time import sleep

from appium import webdriver
from matplotlib import pyplot
from selenium.webdriver.common.by import By


def test_xueqiu():
    caps = {}
    caps["platformName"] = "Android"
    caps["deviceName"] = "127.0.0.1:7555"
    caps["appPackage"] = "com.xueqiu.android"
    caps["appActivity"] = ".view.WelcomeActivityAlias"
    caps['noReset'] = "true"
    caps['chromedriverExecutable'] = "D:/develop/chromedriver/2.20.exe"
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, "//*[@text='交易']").click()
    webview = driver.contexts[-1]
    driver.switch_to.context(webview)
    performance = driver.execute_script("return window.performance.timing")
    print(performance)
    print(performance['responseEnd'] - performance['connectStart'])


logging.basicConfig(level=logging.INFO)


def test_vmstat():
    cmd = "adb shell vmstat"
    res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    logging.info(str(res.stdout.read(), encoding="utf-8").split("\r\n")[2].split()[3])


def test_navigation():
    caps = {}
    caps["platformName"] = "Android"
    caps["deviceName"] = "127.0.0.1:7555"
    caps["appPackage"] = "com.xueqiu.android"
    caps["appActivity"] = ".view.WelcomeActivityAlias"
    caps['noReset'] = "true"
    caps['chromedriverExecutable'] = "D:/develop/chromedriver/2.20.exe"
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, "//*[@text='交易']").click()
    webview = driver.contexts[-1]
    driver.switch_to.context(webview)
    # 查看刚进入页面的操作码：0
    print(driver.execute_script("return window.location.href"))


def test_draw():
    cmd = "adb shell dumpsys gfxinfo com.xueqiu.android"
    res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    lines = res.stdout.readlines()
    i = 1
    # 数据的提取
    for line in lines:
        i += 1
        if "com.xueqiu.android.common.MainActivity" in line.decode("utf-8"):
            break
    # 处理，删除 windows 特殊字符，并提取 120 帧
    lines = [x.decode("utf-8").replace("\r\n", "").replace("\t", " ").strip() for x in lines]
    lines = lines[i:i + 120]
    datas = [[] for row in range(4)]
    # 把四列数据分别存入二维 list
    for x in lines:
        datas[0].append(float(x.split()[0]))
        datas[1].append(float(x.split()[1]))
        datas[2].append(float(x.split()[2]))
        datas[3].append(float(x.split()[3]))
    # 生成画布
    fig = pyplot.figure()
    # 折线图，第一个图片
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(datas[0])
    ax1.set_title("draw")
    # 直方图，第二个图片
    ax1 = fig.add_subplot(2, 2, 2)
    ax1.hist(datas[1], range(5))
    ax1.set_title("prepare")
    # 散点图，第三个图片
    ax1 = fig.add_subplot(2, 2, 3)
    ax1.scatter(range(120), datas[2])
    ax1.set_title("process")
    # 虚线图，第图个图片
    ax1 = fig.add_subplot(2, 2, 4)
    ax1.plot(range(120),datas[3], 'k--')
    ax1.set_title("execute")
    pyplot.show()

