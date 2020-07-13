import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.yield_fixture
def driver():
    if os.environ.get('CI'):
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=options)
    else:
        driver = webdriver.Remote(command_executor='http://127.0.0.1:9515')
    with driver:
        yield driver
