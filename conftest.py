import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from game_setup.models import User


@pytest.yield_fixture(scope="session")
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


@pytest.fixture
def user():
    def action(username, password):
        new_user = User.objects.create_user(username=username, password=password)
        return new_user
    return action


@pytest.fixture
def log_in(driver, live_server):
    def action(username, password):
        driver.get(live_server.url + '/login')
        login_input = driver.find_element_by_css_selector('[data-test="username"]')
        login_input.send_keys(username)
        password_input = driver.find_element_by_css_selector('[data-test="password"]')
        password_input.send_keys(password)
        login_button = driver.find_element_by_css_selector('[data-test="log-in-button"]')
        login_button.click()
    return action


@pytest.fixture
def make_guess():
    def action(guess_value):
        guess_input = driver.find_element_by_css_selector('[data-test="user-guess"]')
        guess_input.send_keys(guess_value)
        make_guess_button = driver.find_element_by_css_selector('[data-test="submit-guess"]')
        make_guess_button.click()
    return action
