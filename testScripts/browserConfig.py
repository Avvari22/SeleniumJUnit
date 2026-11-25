
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def get_browser(browser="chrome", headless=True):

    browser = browser.lower()

    if browser == "chrome":
        options = ChromeOptions()

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()

        if headless:
            options.add_argument("-headless")

        driver = webdriver.Firefox(options=options)

    elif browser == "edge":
        options = EdgeOptions()

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Edge(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    return driver
