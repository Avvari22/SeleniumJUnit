
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_browser(browser):
    browser = browser.lower()
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.maximize_window()
    return driver


def test_login(browser="firefox"):
    driver = get_browser(browser)
    try:
        wait = WebDriverWait(driver, 50)
        driver.get("https://www.saucedemo.com")
        username_input = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()
        
        url = driver.current_url
        assert url == "https://www.saucedemo.com/inventory.html", f"Expected URL: https://www.saucedemo.com/inventory.html, but got: {url}"

        print("TEST PASSED")
        print(f"Browser: {browser}")
        print(f"Title: {driver.title}")
        print(f"URL: {driver.current_url}")
        driver.save_screenshot(f"screenshots - login/{browser}_login_success.png")

    except Exception as e:
        print(f"TEST FAILED: {e}")
        # Capture screenshot when test fails
        driver.save_screenshot("failure_screenshot.png")
        raise
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login("chrome")
    test_login("firefox")
    test_login("edge")
