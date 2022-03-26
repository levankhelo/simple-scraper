from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from chrome import Scraper as chrome_scraper
from firefox import Scraper as firefox_scraper

import time, json

data = {}
browser = "chrome"
# browser = "firefox"

if __name__ == "__main__":
    
    elements = []
    driver = -1
    
    if browser == "chrome":
        driver = chrome_scraper("https://www.nespresso.com/us/en/order/capsules/original")
        WebDriverWait(driver,20)
        elements = driver.find_elements(by=By.CLASS_NAME, value="cn_card")

    if browser == "firefox":
        driver = firefox_scraper("https://www.nespresso.com/us/en/order/capsules/original")
    
    for div in elements:
        values = div.text.splitlines()
        element = {
            "name": values[0],
            "taste": values[1],
            "intensity": values[2],
            "price": {
                "pack": values[3],
                "pod": values[5]
            },
            "includes": values[4]
        }
        data[values[0]] = element
        
    f = open("/etc/data/raw", "w")
    f.write(str(data))
    f.close()
    
    f = open("/etc/data/json", "w")
    f.write(json.dumps(data, sort_keys=True, indent=4))
    f.close()
        
    
    print(data)
    try:
        driver.close()
    except Exception as e:
        print(e)
