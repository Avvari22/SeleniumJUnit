
import os
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from testScripts.browserConfig import get_browser


@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_login(browser):

    driver = get_browser(browser, headless=True)

    os.makedirs("screenshots/login", exist_ok=True)

    try:
        wait = WebDriverWait(driver, 30)

        driver.get("https://www.saucedemo.com/")

        username = wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )

        password = driver.find_element(By.ID, "password")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")

        driver.find_element(By.ID, "login-button").click()

        wait.until(
            EC.url_to_be(
                "https://www.saucedemo.com/inventory.html"
            )
        )

        assert driver.current_url == (
            "https://www.saucedemo.com/inventory.html"
        )

        driver.save_screenshot(
            f"screenshots/login/{browser}_login_success.png"
        )

        print(f"TEST PASSED: {browser}")

    except Exception as e:

        driver.save_screenshot(
            f"screenshots/login/{browser}_failure.png"
        )

        pytest.fail(f"{browser} login failed: {e}")

    finally:
        driver.quit()
