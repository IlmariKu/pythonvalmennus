#!/usr/bin/env python3

import sys
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def install_missing_dependencies():

    asennukset = [
        "selenium",
        "ipykernel",
        "chromedriver-autoinstaller"
    ]

    print("Asennetaan riippuvuuksia...")

    import subprocess
    for asennus in asennukset:
        subprocess.call(
            [sys.executable, "-m", "pip", "--disable-pip-version-check", "install", asennus])


try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import chromedriver_autoinstaller
except ImportError:
    install_missing_dependencies()
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import chromedriver_autoinstaller
except ModuleNotFoundError:
    install_missing_dependencies()
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import chromedriver_autoinstaller


print("Pythonin versio on " +
      str(sys.version_info[0]) + "." + str(sys.version_info[1]))


ASENNUKSET_PATH = __file__.replace(
    "paketit.py", "") + "asennukset/"
CRX_PATH = ASENNUKSET_PATH + 'xpath.crx'


def kaynnista_selain(kaynnista_taustalla=False):

    chromedriver_autoinstaller.install()

    options = Options()
    options.headless = kaynnista_taustalla
    if kaynnista_taustalla is False:
        options.add_extension(CRX_PATH)

    chromeselain = webdriver.Chrome(options=options)

    return chromeselain
