import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import utils.urls as url
from locators.home_page_locators import HomePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Перейти на страницу')
    def navigate(self, page_url: str = url.YA_HOME_PAGE):
        self.driver.get(page_url)

    @allure.step('Получить текущий URL страницы')
    def current_url(self):
        return self.driver.current_url.rstrip('/')

    def find_element(self, locator: tuple[str, str], timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator),
                                                             f"Can't find element by locator {locator}")
        except TimeoutError:
            return None

    def find_elements(self, locator: tuple[str, str], timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator),
                                                             f"Can't find elements by locator {locator}")
        except TimeoutError:
            return None

    def click_element(self, locator: tuple[str, str], timeout: int = 10):
        element = self.find_element(locator, timeout)
        if element:
            element.click()
        else:
            return

    def enter_text(self, locator: tuple[str, str], text: str, timeout: int = 10):
        element = self.find_element(locator, timeout)
        if element:
            element.clear()
            element.send_keys(text)
        else:
            return None

    def element_is_visible(self, locator: tuple[str, str], timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
        except TimeoutError:
            return False

    def element_is_present(self, locator: tuple[str, str], timeout: int = 10):
        try:
            WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))
            return True
        except TimeoutError:
            return False

    def scroll_to_element(self, locator: tuple[str, str], timeout: int = 10):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element(locator))
        self.element_is_visible(locator, timeout)

    @allure.step('Принять cookie')
    def accept_cookies(self):
        self.click_element(HomePageLocators.accept_cookies_button)

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()

    @allure.step('Нажать Enter для завершения выбора')
    def press_enter_button(self, locator: tuple[str, str], timeout: int = 10):
        self.find_element(locator, timeout).send_keys(Keys.ENTER)

    @allure.step('Переключить вкладку по номеру')
    def switch_to(self, window_number: int = 1):
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    @allure.step('Закрыть вкладку')
    def close_page(self):
        self.driver.close()

    @allure.step('Дождаться отображения URL страницы')
    def wait_for_url(self, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until_not(ec.url_matches('about:blank'))
