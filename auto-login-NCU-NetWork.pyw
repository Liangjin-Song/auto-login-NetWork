#!/usr/bin/python3
# Automatic login to NCU campus network by Firefox browser
# writen by Liangjin Song on 20200717
from selenium import webdriver
import time, os, platform
import psutil, re
from datetime import datetime
from selenium.webdriver.firefox.options import Options


# get the boot time duration, the unit is second
def boot_duration():
    return time.time() - psutil.boot_time()


# testing the network
def is_connecting():
    # Judge network connect status
    sys = platform.system()
    if sys == "Windows":
        ping1='ping aaa.ncu.edu.cn'
        ping2='ping www.baidu.com'
    else:
        ping1='ping aaa.ncu.edu.cn -c 2'
        ping2='ping www.baidu.com -c 2'

    pattern = ' TTL='
    result1=os.popen(ping1).read()
    result2=os.popen(ping2).read()
    print(result1)
    print(result2)
    result1=result1.find(pattern)
    result2=result2.find(pattern)

    if result1 != -1:
        if result2 == -1:
            return False

    return True


# login network
def login():
    options = Options()
    options.add_argument('--headless')

    url = 'https://aaa.ncu.edu.cn'
    browser = webdriver.Firefox(options=options)

    # open the url by Firefox
    browser.get(url)

    # waiting 5 seconds to load script
    browser.implicitly_wait(5)

    # input the information
    username = browser.find_element_by_id('username')
    username.send_keys('replace with username')
    password = browser.find_element_by_id('password')
    password.send_keys('replace with password')

    # click the login button
    login_button = browser.find_element_by_id('login')
    login_button.click()

    # waiting 5 seconds, and refreshing the page
    time.sleep(5)
    browser.get(url)

    # closing the browser
    browser.quit()


def main():
    # sleep time, the unit is minute
    sleep_time = 5

    while True:
        if boot_duration() > 300:
            while not is_connecting():
                login()
            print('sleeping......')
            time.sleep(sleep_time * 60)
        else:
            print('sleeping......')
            time.sleep(300)


if __name__ == '__main__':
    main()

