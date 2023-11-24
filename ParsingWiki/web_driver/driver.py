from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Webdriver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--incognito")
    options.add_argument("--disable-cache")
    # options.add_argument("--window-size=1920,1080")
    options.page_load_strategy = "eager"
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    s = Service()
    browser = webdriver.Chrome(options=options, service=s)

    browser.get('https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites')