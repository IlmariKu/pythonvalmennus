import csv
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from kaynnistys import kaynnista_selain


selain = kaynnista_selain()
selain.get("https://ilmariku.github.io/") # Kirjoita osoite osoite-kenttään ja mene selaimella sinne

time.sleep(10)
selain.close()
selain.quit()

