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
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "ipykernel"])
    import wget
    from selenium.webdriver import Chrome
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.keys import Keys


class PlatformError(Exception):
    pass


# ChromeDriver, version 91.0.4472.19
BASE_URL = "https://chromedriver.storage.googleapis.com/90.0.4430.24/"
MAC_CHROME = "chromedriver_mac64.zip"
WINDOWS_CHROME = "chromedriver_mac64.zip"
LINUX_CHROME = "chromedriver_linux64.zip"
ASENNUKSET_PATH = __file__.replace(
    "paketit.py", "") + "asennukset/"
CHROMEDRIVER_PATH = ASENNUKSET_PATH + "chromedriver"
CRX_PATH = ASENNUKSET_PATH + 'xpath.crx'


def kaynnista_selain(kaynnista_taustalla=False):

    check_and_get_chromedriver()

    def wrong_spelling(komennossa_on_s_liikaa=""):
        print("Valitsit komennon vahingossa väärin. Poista kirjoittamastasi komennosta -s kirjain lopusta. element, ei elements")

    options = Options()
    options.headless = kaynnista_taustalla
    options.add_extension(CRX_PATH)

    chromeselain = Chrome(executable_path=CHROMEDRIVER_PATH, options=options)

    chromeselain.find_elements_by_class_name = wrong_spelling
    chromeselain.find_elements_by_css_selector = wrong_spelling
    chromeselain.find_elements_by_id = wrong_spelling
    chromeselain.find_elements_by_link_text = wrong_spelling
    chromeselain.find_elements_by_name = wrong_spelling
    chromeselain.find_elements_by_partial_link_text = wrong_spelling
    chromeselain.find_elements_by_tag_name = wrong_spelling
    chromeselain.find_elements_by_xpath = wrong_spelling

    return chromeselain


def check_and_get_chromedriver():
    def is_chromedriver_installed():
        return os.path.isfile(CHROMEDRIVER_PATH)

    def unzip_chromedriver(ZIP_PATH):
        try:
            with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
                zip_ref.extractall(ASENNUKSET_PATH)
        except FileNotFoundError:
            return
        os.remove(ZIP_PATH)

    if is_chromedriver_installed() is True:
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

    wget.download(BASE_URL + CHROME_OS, ASENNUKSET_PATH)
    unzip_chromedriver(ASENNUKSET_PATH + "/" + CHROME_OS)

    if operating_system == "Darwin" or operating_system == "Linux":
        # Mac-specific, giving broad-permissions to file
        os.chmod(CHROMEDRIVER_PATH, 755)


check_and_get_chromedriver()
