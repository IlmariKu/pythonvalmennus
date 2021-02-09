import os
import platform
import wget
import zipfile
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

class PlatformError(Exception):
    pass


# ChromeDriver, version 88.0.4324.96
BASE_URL = "https://chromedriver.storage.googleapis.com/88.0.4324.96/"
MAC_CHROME = "chromedriver_mac64.zip"
WINDOWS_CHROME = "chromedriver_mac64.zip"
LINUX_CHROME = "chromedriver_linux64.zip"


def kaynnista_selain(kaynnista_taustalla=False):
    options = Options()
    options.headless = kaynnista_taustalla

    #path = "/Users/ilmari/koodi/chromedriver/chromedriver"

    return Chrome(
        executable_path=path,
        options=options
    )


def check_and_get_chromedriver():
    current_path = os.getcwd()
    operating_system = platform.system()
    if operating_system == "Darwin": # MacOS
        CHROME_OS = MAC_CHROME
    elif operating_system == "Windows":
        CHROME_OS = WINDOWS_CHROME
    elif operating_system == "Linux": # MacOS
        CHROME_OS = LINUX_CHROME
    else:
        raise PlatformError("Platform " + str(operating_system) + " is not recognized")

    wget.download(BASE_URL + CHROME_OS)

    with zipfile.ZipFile(os.getcwd() + "/" + CHROME_OS, 'r') as zip_ref:
        zip_ref.extractall("selainosat")

    # Pura tiedosto
    with zipfile.ZipFile("file.zip","r") as zip_ref:
        zip_ref.extractall("targetdir")

check_and_get_chromedriver()
