
import pytest
from pathlib import Path
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():

    options = Options()

    # Headless browser execution
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    browser = webdriver.Chrome(options=options)

    yield browser

    browser.quit()
    
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)

@pytest.fixture(autouse=True)
def capture_failure_screenshot(request, driver):

    yield

    report = getattr(request.node, "rep_call", None)

    if report and report.failed:

        Path("screenshots").mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        filename = (
            f"{request.node.name}_{timestamp}.png"
        )

        filepath = Path("screenshots") / filename

        driver.save_screenshot(str(filepath))

        print(f"Failure screenshot: {filepath}")
