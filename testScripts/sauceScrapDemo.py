
import csv
import os
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from testScripts.browserConfig import get_browser


def test_scrape_saucedemo():

    driver = get_browser("chrome", headless=True)

    try:
        wait = WebDriverWait(driver, 30)

        driver.get("https://www.saucedemo.com/")

        wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")

        driver.find_element(
            By.ID, "password"
        ).send_keys("secret_sauce")

        driver.find_element(
            By.ID, "login-button"
        ).click()

        wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item")
            )
        )

        products = driver.find_elements(
            By.CLASS_NAME, "inventory_item"
        )

        scraped_data = []

        for product in products:

            scraped_data.append({
                "Product Name": product.find_element(
                    By.CLASS_NAME, "inventory_item_name"
                ).text,

                "Description": product.find_element(
                    By.CLASS_NAME, "inventory_item_desc"
                ).text,

                "Price": product.find_element(
                    By.CLASS_NAME, "inventory_item_price"
                ).text,

                "Image URL": product.find_element(
                    By.CSS_SELECTOR, ".inventory_item_img img"
                ).get_attribute("src")
            })

        os.makedirs("reports", exist_ok=True)

        with open(
            "reports/saucedemo_products.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            fieldnames = [
                "Product Name",
                "Description",
                "Price",
                "Image URL"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(scraped_data)

        assert len(scraped_data) > 0

        print(f"Successfully scraped {len(scraped_data)} products")

    except Exception as e:

        os.makedirs("screenshots", exist_ok=True)

        driver.save_screenshot(
            "screenshots/scraping_failure.png"
        )

        pytest.fail(f"Scraping failed: {e}")

    finally:
        driver.quit()
