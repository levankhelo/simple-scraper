from selenium.webdriver.chrome.options import Options
from selenium import webdriver

class Scraper:
    def __init__(self, link, headless=False):
        return self.scrape(link)
    
    def set_options(headless = False) -> None:
        """Sets chrome options for Selenium.
        Chrome options for headless browser is enabled.
        """
        chrome_options = Options()
        if( headless != False ):
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_prefs = {}
        chrome_options.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        return chrome_options
    
    def scrape(self, link, headless):
        driver = webdriver.Chrome( options = self.set_options(headless) )
        driver.get(link)
        self.driver = driver
        return driver
        