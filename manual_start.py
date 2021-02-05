import selenium
import os
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = False

# My local path
path = "/Users/ilmari/koodi/chromedriver/chromedriver"

selain = Chrome(
    executable_path=path,
    options=options
)

base_url = "http://yle.fi"
selain.get(base_url)
