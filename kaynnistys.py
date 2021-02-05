import os
import csv
import time
import selenium
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def kaynnista_selain(kaynnista_taustalla=False):
    options = Options()
    options.headless = kaynnista_taustalla

    path = "/Users/ilmari/koodi/chromedriver/chromedriver"

    return Chrome(
        executable_path=path,
        options=options
    )
