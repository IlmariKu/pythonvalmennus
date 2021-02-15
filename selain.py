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
CHROMEDRIVER_PATH = os.getcwd() + "/asennukset/chromedriver"


def kaynnista_selain(kaynnista_taustalla=False):

    check_and_get_chromedriver()

    options = Options()
    options.headless = kaynnista_taustalla

    return Chrome(
        executable_path=CHROMEDRIVER_PATH,
        options=options
    )


def check_and_get_chromedriver():

    def is_chromedriver_installed():
        return os.path.isfile(os.getcwd() + "/asennukset/chromedriver")

    if is_chromedriver_installed() is True:
        return

    print("Asennetaan vaadittuja paketteja...")
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
    ZIP_PATH = os.getcwd() + "/" + CHROME_OS

    with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
        zip_ref.extractall("asennukset")

    os.remove(ZIP_PATH)

    if operating_system == "Darwin" or operating_system == "Linux":
        os.chmod(CHROMEDRIVER_PATH, 755) # Mac-specific, giving broad-permissions to file


check_and_get_chromedriver()
