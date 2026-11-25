
import csv
import pytest

from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# CSV file location
CSV_FILE = (
    Path(__file__).resolve().parent.parent
    / "test_data"
    / "saucedemo_products.csv"
)


# Step 1: Validate CSV headers and load test data
def load_test_data():

    expected_headers = [
        "Product Name",
        "Description",
        "Price",
        "Image URL"
    ]

    with open(
        CSV_FILE,
        mode="r",
        encoding="utf-8-sig",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        actual_headers = reader.fieldnames

        # Validate CSV headers
        assert actual_headers == expected_headers, (
            f"CSV header mismatch!\n"
            f"Expected: {expected_headers}\n"
            f"Actual: {actual_headers}"
        )

        # Read data using exact CSV header names
        test_data = []

        for row in reader:

            test_data.append(
                (
                    row["Product Name"].strip(),
                    row["Description"].strip(),
                    float(row["Price"].replace("$", "").strip()),
                    row["Image URL"].strip()
                )
            )

        assert test_data, "No test data found in CSV"

        return test_data


# Step 2: Parameterize test cases
@pytest.mark.parametrize(
    "product_name, description, expected_price, image_url",
    load_test_data()
)
def test_product_price_verification(
    driver,
    product_name,
    description,
    expected_price,
    image_url
):

    wait = WebDriverWait(driver, 15)

    # Step 3: Open SauceDemo
    driver.get("https://www.saucedemo.com/")

    # Step 4: Login
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

    # Step 5: Wait for inventory page
    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )

    # Step 6: Find matching product
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

    # Step 7: Verify product exists
    assert matching_product is not None, (
        f"Product not found: {product_name}"
    )

    # Step 8: Validate product description
    actual_description = matching_product.find_element(
        By.CLASS_NAME, "inventory_item_desc"
    ).text

    assert actual_description == description, (
        f"Description mismatch for {product_name}"
    )

    # Step 9: Validate product price
    actual_price_text = matching_product.find_element(
        By.CLASS_NAME, "inventory_item_price"
    ).text

    actual_price = float(
        actual_price_text.replace("$", "")
    )

    assert actual_price == pytest.approx(
        expected_price,
        abs=0.001
    ), (
        f"Price mismatch for {product_name}. "
        f"Expected: ${expected_price}, "
        f"Actual: ${actual_price}"
    )

    # Step 10: Validate product image URL
    actual_image_url = matching_product.find_element(
        By.CSS_SELECTOR, ".inventory_item_img img"
    ).get_attribute("src")

    assert actual_image_url.rstrip("/") == image_url.rstrip("/"), (
        f"Image URL mismatch for {product_name}. "
        f"Expected: {image_url}, Actual: {actual_image_url}"
    )

    # Step 11: Capture screenshot
    screenshot_dir = Path("screenshots")
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    safe_product_name = "".join(
        c if c.isalnum() or c in "-_" else "_"
        for c in product_name
    )

    driver.save_screenshot(
        str(screenshot_dir / f"{safe_product_name}.png")
    )

    print(
        f"\nPASS: {product_name} | "
        f"Price: ${actual_price} | "
        f"Description: Validated | "
        f"Image URL: Validated"
    )
