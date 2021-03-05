# Second phase

import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from selain import kaynnista_selain


##########
################### KOODI ALKAA ###########################
##########

# Käynnistä selain ja mene osoitteeseen
selain = kaynnista_selain()
selain.get("https://ilmariku.github.io")

time.sleep(3)  # Odota kolme sekuntia

# Etunimi
etunimi = '//*[@id="fname"]' # Etsi hakukenttä
selain.find_element_by_xpath(etunimi).send_keys("Jussi") # Kirjoita etunimi

# Sukunimi
etunimi = '//*[@id="lname"]' # Etsi hakukenttä
selain.find_element_by_xpath(etunimi).send_keys("Kuontare") # Kirjoita etunimi

# Ei uutiskirjettä
uutiskirje = "/html/body/form/label[7]"
selain.find_element_by_xpath(etunimi).click() # Kirjoita etunimi
