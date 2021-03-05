import csv
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from selain import kaynnista_selain


##########
################### KOODI ALKAA ###########################
##########

# Käynnistä selain ja mene osoitteeseen
selain = kaynnista_selain()
selain.get("https://verkkokauppa.com")


# Hakukenttä & haku
time.sleep(5) # Odota viisi sekuntia, että sivu latautuu
hakuboksi = "/html/body/div[1]/div[1]/header/div/nav/form/div/input" # Etsi hakukenttä
selain.find_element_by_xpath(hakuboksi).send_keys("Macbook pro") # Etsi hakukenttä ja kirjoita hakukenttään sanat Macbook pro
selain.find_element_by_xpath(hakuboksi).send_keys(Keys.RETURN) # Etsi hakukenttä ja paina enteriä


# Ota ensimmäisen Macbookin hinta
time.sleep(5) # Odota viisi sekuntia
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
