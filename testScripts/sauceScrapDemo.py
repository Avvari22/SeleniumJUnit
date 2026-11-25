
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


def scrape_saucedemo():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    try:
        # Open website
        driver.get("https://www.saucedemo.com/")

        # Login
        wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")

        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Wait for inventory page
        wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item")
            )
        )

        # Extract products
        products = driver.find_elements(
            By.CLASS_NAME, "inventory_item"
        )

        scraped_data = []

        for product in products:

            name = product.find_element(
                By.CLASS_NAME, "inventory_item_name"
            ).text

            description = product.find_element(
                By.CLASS_NAME, "inventory_item_desc"
            ).text

            price = product.find_element(
                By.CLASS_NAME, "inventory_item_price"
            ).text

            image = product.find_element(
                By.CLASS_NAME, "inventory_item_img"
            ).find_element(By.TAG_NAME, "img").get_attribute("src")

            scraped_data.append({
                "Product Name": name,
                "Description": description,
                "Price": price,
                "Image URL": image
            })

        # Display results
        print("\n--- SCRAPED PRODUCT DATA ---\n")

        for item in scraped_data:
            print(item)

        # Export to CSV
        with open(
            "saucedemo_products.csv",
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

        print(f"\nSuccessfully scraped {len(scraped_data)} products.")
        print("CSV file created: saucedemo_products.csv")

    except Exception as e:
        print("Scraping failed:", e)
        driver.save_screenshot("scraping_failure.png")
        raise

    finally:
        driver.quit()


if __name__ == "__main__":
    scrape_saucedemo()
