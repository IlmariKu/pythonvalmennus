import sys

asennukset = [
    "selenium",
    "ipykernel"
    "chromedriver-autoinstaller"
]

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import chromedriver_autoinstaller
except ImportError:
    import subprocess
    for asennus in asennukset:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", asennus])
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import chromedriver_autoinstaller

ASENNUKSET_PATH = __file__.replace(
    "paketit.py", "") + "asennukset/"
CRX_PATH = ASENNUKSET_PATH + 'xpath.crx'


def kaynnista_selain(kaynnista_taustalla=False):

    def wrong_spelling(komennossa_on_s_liikaa=""):
        print("Valitsit komennon vahingossa väärin. Poista kirjoittamastasi komennosta -s kirjain lopusta. element, ei elements")

    chromedriver_autoinstaller.install()

    options = Options()
    options.headless = kaynnista_taustalla
    options.add_extension(CRX_PATH)

    chromeselain = webdriver.Chrome(options=options)

    chromeselain.find_elements_by_class_name = wrong_spelling
    chromeselain.find_elements_by_css_selector = wrong_spelling
    chromeselain.find_elements_by_id = wrong_spelling
    chromeselain.find_elements_by_link_text = wrong_spelling
    chromeselain.find_elements_by_name = wrong_spelling
    chromeselain.find_elements_by_partial_link_text = wrong_spelling
    chromeselain.find_elements_by_tag_name = wrong_spelling
    chromeselain.find_elements_by_xpath = wrong_spelling

    return chromeselain
