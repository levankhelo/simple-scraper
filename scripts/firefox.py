from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class Scraper:
    def __init__(self, link, headless=False):
        self.scrape(link, headless)

    def set_options(headless = False) -> None:
        firefox_options = Options()
        firefox_options.headless = headless
        firefox_options.log.level = "trace"
    
    def set_profile() -> None:
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.cache.disk.enable", False)
        profile.set_preference("browser.cache.memory.enable", False)
        profile.set_preference("browser.cache.offline.enable", False)
        profile.set_preference("network.http.use-cache", False)
        profile.set_preference("general.useragent.override","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0")
        return profile

    def scrape(self, link, headless=False):
        ff_opt = {
            "firefox_binary":FirefoxBinary('/opt/firefox/firefox'),
		    "firefox_profile":self.set_profile,
		    "options":self.set_options,
		    "service_log_path":'/geckodriver.log'
        }
        
        driver = webdriver.Firefox(**ff_opt)
        driver.get(link)
        self.driver = driver
        return driver
