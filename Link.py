from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import pyautogui
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import urllib.request
from selenium.webdriver.chrome.options import Options 
import clipboard
import time
import io
from PIL import Image
import urllib

def getlinkfromkw(kw, driver):
    imagenumber = 1
    link = ""
    while imagenumber <= 10:
        url = f"https://www.google.com/search?q={kw}%20&tbm=isch&hl=en&hl=en&safe=active&safe=active&tbs=isz%3Alt%2Cislt%3Axga%2Csur%3Afc&ved=0CAEQpwVqFwoTCJiHvcaN0OoCFQAAAAAdAAAAABAC&biw=1905&bih=949"
        driver.get(url)
        time.sleep(1)
        firstimageid = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[{}]".format(imagenumber)).get_attribute("data-id")
        # print(firstimageid)
        driver.get(url+"#imgrc={}".format(firstimageid))
        largerimage = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img")
        time.sleep(2)
        action = ActionChains(driver)
        action.context_click(largerimage).perform()
        pyautogui.press(['down'], presses=9)
        pyautogui.press(['enter'])

        link = clipboard.paste()
        try:
            urllib.request.urlretrieve(link)
            imageweb = urllib.request.urlopen(link)
            imagefilename = io.BytesIO(imageweb.read())
            Image.open(imagefilename)
            break
        except:
            imagenumber += 1

    return link
