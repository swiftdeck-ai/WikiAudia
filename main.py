from google.cloud import texttospeech
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains

import pyautogui
import clipboard
import urllib.request

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getcwd() + "/credentials.json"


def saveImagebySearch(keyword, driver):
    url = "https://www.google.com/search?as_st=y&tbm=isch&hl=en&as_q=" + keyword + "&as_epq=&as_oq=&as_eq=&cr=&as_sitesearch=&safe=active&tbs=isz:lt,islt:xga"

    driver.get(url)
    image = driver.find_element_by_xpath("//*[@id=\"islrg\"]/div[1]/div[1]/a[1]/div[1]/img")
    image.click()
    enlarged = driver.find_element_by_xpath(
        "//*[@id=\"Sva75c\"]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img")
    actionChains = ActionChains(driver)
    actionChains.context_click(enlarged).perform()
    pyautogui.press(['down'], presses=10)
    pyautogui.press(['enter'])
    imagelocation = clipboard.paste()
    urllib.request.urlretrieve(imagelocation, "downloads/{}.jpg".format(''.join(keyword.title().split())))


def synthesizeText(text):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.MALE, name="en-US-Wavenet-D",
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)


if __name__ == "__main__":
    driverOuter = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    saveImagebySearch("Python", driverOuter)
    driverOuter.quit()
    # synthesizeText('Google Cloud Text-to-Speech enables developers to synthesize natural-sounding speech with 100+ voices, available in multiple languages and variants. It applies DeepMind’s groundbreaking research in WaveNet and Google’s powerful neural networks to deliver the highest fidelity possible. As an easy-to-use API, you can create lifelike interactions with your users, across many applications and devices.')
