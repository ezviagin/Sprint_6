import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
