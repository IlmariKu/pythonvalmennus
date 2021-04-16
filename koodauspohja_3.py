import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from selain import kaynnista_selain
selain = kaynnista_selain()

#################################
##########
################### KOODI ALKAA ###########################
##########
#################################


#################################
##########
################### KOODI LOPPUU ###########################
##########
#################################
sulje_selain_lopuksi = "kylla"
if sulje_selain_lopuksi == "kylla":
    selain.close()
    selain.quit()
