import csv
import time
from selain import kaynnista_selain

selain = kaynnista_selain()
selain.get("https://ilmariku.github.io/asennusonnistui.html")
time.sleep(10)
selain.close()
selain.quit()
