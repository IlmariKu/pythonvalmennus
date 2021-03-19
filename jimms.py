import csv
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from selain import kaynnista_selain

##########
################### KOODI ALKAA ###########################
##########


selain = kaynnista_selain()
# Kirjoita osoite osoite-kenttään ja mene selaimella sinne
selain.get("https://jimms.fi")


# Hakukenttä & haku
time.sleep(5)  # Odota viisi sekuntia, että sivu latautuu
hakuboksi = '//*[@id="qpsv2-topinput"]'  # Etsi hakukenttä
# Etsi hakukenttä ja kirjoita hakukenttään sanat Macbook pro
selain.find_element_by_xpath(hakuboksi).send_keys(
    "Macbook Pro 13 tietokone hopea 512GB M1")
selain.find_element_by_xpath(hakuboksi).send_keys(
    Keys.RETURN)  # Etsi hakukenttä ja paina enteriä


# Etsi ensimmäinen Macbook
time.sleep(5)  # Odota viisi sekuntia
ensimmainen_hakutulos = "/html/body/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[3]/div[1]/a/span"
selain.find_element_by_xpath(ensimmainen_hakutulos).click()
time.sleep(5)  # Odotetaan, että sivu latautuu


# Otetaan koneen hinta, toimitusaika-arvio ja saatavuus
koneen_nimi_sivulla = "/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/h1"
hinta_sivulla = "/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[1]/span/span/span[1]"
lahetystiedot_sivulla = "/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[3]"
saatavuus_sivulla = "/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]"

# Hae tiedot jokaisesta kohdasta
kone = selain.find_element_by_xpath(koneen_nimi_sivulla).text
hinta = selain.find_element_by_xpath(hinta_sivulla).text
toimitusaika = selain.find_element_by_xpath(lahetystiedot_sivulla).text
saatavuus = selain.find_element_by_xpath(saatavuus_sivulla).text

# Tulosta tiedot näkyväksi
print("\n\n\n")  # Tyhjää tilaa koodin jälkeen, jotta on helpompi nähdä
print("Tietokone: " + kone)
print("Kneen hinta: " + hinta)
print("Toimitusaika-arvio: " + toimitusaika)
print("Saatavuus tukkurilla: " + saatavuus)

# Otetaan screenshot näytöstä
selain.save_screenshot("kuva-tietokoneista.png")

# Sulje selain, kun olet ajanut ohjelman
selain.close()
selain.quit()
