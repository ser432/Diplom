import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://ru.yougile.com/api-v2"
YOUGILE_TOKEN = "YOUR_API_TOKEN_HERE"

@pytest.fixture(scope="session")
def api_headers():
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {YOUGILE_TOKEN}"
    }

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
