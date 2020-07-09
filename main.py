from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains

import pyautogui
import clipboard
import urllib.request


def saveImagebySearch(keyword,driver):

    url = "https://www.google.com/search?as_st=y&tbm=isch&hl=en&as_q="+keyword+"&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=&safe=active&tbs=isz:lt,islt:xga"
    
    driver.get(url)
    image = driver.find_element_by_xpath("//*[@id=\"islrg\"]/div[1]/div[1]/a[1]/div[1]/img")
    image.click()
    enlarged = driver.find_element_by_xpath("//*[@id=\"Sva75c\"]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img")
    actionChains = ActionChains(driver)
    actionChains.context_click(enlarged).perform()
    pyautogui.press(['down'], presses=10)
    pyautogui.press(['enter'])
    imagelocation = clipboard.paste()
    urllib.request.urlretrieve(imagelocation, "downloads/{}.jpg".format(''.join(keyword.title().split())))


if __name__ == "__main__":
    driverOuter = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    saveImagebySearch("INSERT_KEYWORD_HERE", driverOuter)
    driverOuter.quit()
    
