import os
import csv
import time
import selenium
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.headless = False

# Käynnistyspolku
path = "/Users/ilmari/koodi/chromedriver/chromedriver"

selain = Chrome(
    executable_path=path,
    options=options
)

################### KOODI ALKAA ###########################

selain.get("https://verkkokauppa.com") # Kirjoita osoite osoite-kenttään ja mene selaimella sinne

# Hakukenttä & haku
time.sleep(5) # Odota viisi sekuntia, että sivu latautuu
hakuboksi = "/html/body/div[1]/div[1]/header/div/nav/form/div/input" # Etsi hakukenttä
selain.find_element_by_xpath(hakuboksi).send_keys("Macbook pro") # Etsi hakukenttä ja kirjoita hakukenttään sanat Macbook pro
selain.find_element_by_xpath(hakuboksi).send_keys(Keys.RETURN) # Etsi hakukenttä ja paina enteriä

# Ota ensimmäisen Macbookin hinta

time.sleep(5) # Odota kolme sekuntia, että sivu latautuu
ensimmainen_hakutulos = "/html/body/div[1]/div[1]/div/div/main/div/div[6]/div/ol[1]/li[1]/div/div[1]/div/a"
selain.find_element_by_xpath(hakuboksi).click()

eka_kone = "/html/body/div[1]/div[1]/div/div/main/div/div[6]/div/ol[1]/li[1]/div/div[1]/div/a"
toka_kone = "/html/body/div[1]/div[1]/div/div/main/div/div[6]/div/ol[1]/li[2]/div/div[1]/div/a"

selain.find_element_by_xpath(eka_kone).click()
hinta_kohta = "/html/body/div[1]/div[1]/div/div/main/section/aside/div[2]/div[1]/div[2]/div[1]/span/data"
lahetystiedot_kohta = "/html/body/div[1]/div[1]/div/div/main/section/aside/div[2]/div[2]/div[1]/div[1]/span"
ekan_koneen_hinta = selain.find_element_by_xpath(hinta_kohta).text
ekan_koneen_lahetystiedot = selain.find_element_by_xpath(lahetystiedot_kohta)





selain.close()
selain.quit()
