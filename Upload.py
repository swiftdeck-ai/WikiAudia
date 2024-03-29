from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from webdriver_manager.chrome import ChromeDriverManager


def uploadvideo(video, subs, title, description, thumbnail, language, full=False):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(
        "https://studio.youtube.com/channel/UCsLCKPmJXsDh90Eum8eMZXw/videos/upload?d=ud&filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D")
    time.sleep(2)
    usernameField = driver.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
    usernameField.send_keys("wikiaudiayt@gmail.com")
    usernameNext = driver.find_element_by_xpath("//*[@id=\"identifierNext\"]/div/button")
    usernameNext.click()
    time.sleep(1)
    passwordField = driver.find_element_by_xpath("//*[@id=\"password\"]/div[1]/div/div[1]/input")
    passwordField.send_keys("w1k1p3d1a12345!@#$%")
    passwordNext = driver.find_element_by_xpath("//*[@id=\"passwordNext\"]/div/button")
    passwordNext.click()
    time.sleep(2)
    fileInput = driver.find_element_by_xpath("//*[@id=\"content\"]/input")
    fileInput.send_keys(os.path.abspath(video))
    time.sleep(5)
    videoTitle = driver.find_element_by_xpath("//*[@id=\"textbox\"]")
    i = 0
    while i < 50:
        videoTitle.send_keys(Keys.BACKSPACE)
        i += 1
    videoTitle.send_keys(title.title())
    videoDescription = driver.find_element_by_xpath(
        "/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-details/div/ytcp-uploads-basics/ytcp-mention-textbox[2]/ytcp-form-input-container/div[1]/div[2]/ytcp-mention-input/div")
    videoDescription.send_keys(description)
    videoThumbnail = driver.find_element_by_xpath(
        "/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-details/div/ytcp-uploads-basics/ytcp-thumbnails-compact-editor/div[3]/ytcp-thumbnails-compact-editor-uploader/input")
    videoThumbnail.send_keys(os.path.abspath(thumbnail))
    playlist = driver.find_element_by_xpath(
        "/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-details/div/ytcp-uploads-basics/ytcp-video-metadata-playlists/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger/div/div[3]/iron-icon")
    playlist.click()
    done = driver.find_element_by_xpath("/html/body/ytcp-playlist-dialog/paper-dialog/div[2]/ytcp-button[3]/div")
    if language == 'hi' and full:
        fullHindi = driver.find_element_by_xpath("//*[text()[contains(.,'Full Videos - Hindi')]]")
        fullHindi.click()
        done.click()
    elif language == 'hi' and not full:
        summaryHindi = driver.find_element_by_xpath("//*[text()[contains(.,'Summary Videos - Hindi')]]")
        summaryHindi.click()
        done.click()
    elif language == 'en' and full:
        fullEnglish = driver.find_element_by_xpath("//*[text()[contains(.,'Full Videos - English')]]")
        fullEnglish.click()
        done.click()
    elif language == 'en' and not full:
        summaryEnglish = driver.find_element_by_xpath("//*[text()[contains(.,'Summary Videos - English')]]")
        summaryEnglish.click()
        done.click()

    kidsOption = driver.find_element_by_xpath(
        "/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-details/div/ytcp-uploads-basics/ytcp-form-audience/ytcp-audience-picker/div[3]/paper-radio-group/paper-radio-button[2]/div[1]")
    kidsOption.click()
    moreOptions = driver.find_element_by_xpath(
        "/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-details/div/div/ytcp-button")
    moreOptions.click()
    chooseSubLanguage = driver.find_element_by_xpath(
        "/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-details/div/ytcp-uploads-advanced/div[4]/ytcp-form-language-input/ytcp-form-select/ytcp-select/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger")
    chooseSubLanguage.click()
    subLanguage = driver.find_element_by_xpath(
        "/html/body/ytcp-text-menu/paper-dialog/paper-listbox/paper-item[45]") if language == "en" else driver.find_element_by_xpath(
        "/html/body/ytcp-text-menu/paper-dialog/paper-listbox/paper-item[78]")
    subLanguage.click()
    time.sleep(2)
    chooseSubFile = driver.find_element_by_xpath(
        "/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-details/div/ytcp-uploads-advanced/ytcp-video-metadata-captions/div/div/ytcp-button")
    chooseSubFile.click()
    driver.find_element_by_xpath(
        "/html/body/ytcp-video-metadata-captions-upload-dialog/ytcp-dialog/paper-dialog/div[3]/div/ytcp-button[2]").click()
    subFile = driver.find_element_by_xpath("//*[@id=\"captions-file-loader\"]")
    subFile.send_keys(os.path.abspath(subs))
    time.sleep(1)
    nextPage = driver.find_element_by_xpath(
        "/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]")
    nextPage.click()
    time.sleep(1)
    nextPage.click()
    privateButton = driver.find_element_by_xpath(
        "/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]/paper-radio-group/paper-radio-button[1]/div[1]/div[1]")
    privateButton.click()
    saveButton = driver.find_element_by_xpath(
        "/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]")
    saveButton.click()
    time.sleep(10)
    driver.quit()