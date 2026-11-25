
import csv
import pytest

from selenium import webdriver
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Read test data from CSV
CSV_FILE = (
    Path(__file__).resolve().parent
    / "test_data"
    / "saucedemo_products.csv"
)


def load_test_data():

    with open(CSV_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        return [
            (
                row["Product Name"],
                float(row["Price"].replace("$", ""))
            )
            for row in reader
        ]


# Parameterize test cases using CSV data
@pytest.mark.parametrize(
    "Product Name, Price",
    load_test_data()
)
def test_product_price_verification(
    driver,
    product_name,
    expected_price
):

    wait = WebDriverWait(driver, 15)

    # Step 1: Open SauceDemo
    driver.get("https://www.saucedemo.com/")

    # Step 2: Login
    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "user-name")
        )
    ).send_keys("standard_user")

    driver.find_element(
        By.ID, "password"
    ).send_keys("secret_sauce")

    driver.find_element(
        By.ID, "login-button"
    ).click()

    # Step 3: Wait for inventory
    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )
    	
    driver.save_screenshot(f"screenshots/{product_name}")

    # Step 4: Find matching product
    products = driver.find_elements(
        By.CLASS_NAME, "inventory_item"
    )

    matching_product = None

    for product in products:

        name = product.find_element(
            By.CLASS_NAME, "inventory_item_name"
        ).text

        if name == product_name:
            matching_product = product
            break

    # Step 5: Validate product exists
    assert matching_product is not None, (
        f"Product not found: {product_name}"
    )

    # Step 6: Extract actual price
    actual_price_text = matching_product.find_element(
        By.CLASS_NAME, "inventory_item_price"
    ).text

    actual_price = float(
        actual_price_text.replace("$", "")
    )

    # Step 7: Verify expected vs actual price
    assert actual_price == pytest.approx(
        expected_price, abs=0.001
    ), (
        f"Price mismatch for {product_name}. "
        f"Expected: ${expected_price}, "
        f"Actual: ${actual_price}"
    )

    print(
        f"PASS: {product_name} | "
        f"Expected: ${expected_price} | "
        f"Actual: ${actual_price}"
    )
    
if __name__ == "__main__":
	test_product_price_verification(webdriver.Chrome(),"Sauce Labs Backpack", 29.99)
