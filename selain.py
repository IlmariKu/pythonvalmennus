import os
import sys
import platform
import zipfile
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

try:
    import wget
    from selenium.webdriver import Chrome
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.keys import Keys
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "selenium"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "wget"])
    import wget
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
ASENNUKSET_PATH = __file__.replace(
    "selain.py", "") + "/asennukset/"
CHROMEDRIVER_PATH = ASENNUKSET_PATH + "chromedriver"


def kaynnista_selain(kaynnista_taustalla=False):

    check_and_get_chromedriver()

    options = Options()
    options.headless = kaynnista_taustalla
    return Chrome(executable_path=CHROMEDRIVER_PATH, options=options)


def check_and_get_chromedriver():
    def is_chromedriver_installed():
        return os.path.isfile(CHROMEDRIVER_PATH)

    def unzip_chromedriver(ZIP_PATH):
        with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
            zip_ref.extractall(ASENNUKSET_PATH)
        os.remove(ZIP_PATH)

    if is_chromedriver_installed() is True:
        print("\n Chromedriver on asennettu tietokoneellesi oikein.")
        return

    print("Asennetaan vaadittuja paketteja...")
    operating_system = platform.system()
    if operating_system == "Darwin":  # MacOS
        CHROME_OS = MAC_CHROME
    elif operating_system == "Windows":
        CHROME_OS = WINDOWS_CHROME
    elif operating_system == "Linux":  # MacOS
        CHROME_OS = LINUX_CHROME
    else:
        raise PlatformError(
            "Platform " + str(operating_system) + " is not recognized")

    wget.download(BASE_URL + CHROME_OS)
    unzip_chromedriver(os.getcwd() + "/" + CHROME_OS)

    if operating_system == "Darwin" or operating_system == "Linux":
        # Mac-specific, giving broad-permissions to file
        os.chmod(CHROMEDRIVER_PATH, 755)


check_and_get_chromedriver()
