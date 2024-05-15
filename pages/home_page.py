import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as wait

from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class YaScooterHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Прокрутить до элемента страницы')
    def scroll_to_question_about_important_section(self):
        self.scroll_to_element(HomePageLocators.questions_about_important_title)

    @allure.step('Нажать на один из вопросов списка')
    def click_question_buttons(self, question_id: int):
        elements = self.find_elements(HomePageLocators.question_buttons, 10)
        elements[question_id].click()
        wait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH,
                                    f".//div[@id='accordion__panel-{question_id}' and not(@hidden)]")))

    @allure.step('Нажать на логотип "Yandex"')
    def click_yandex_logo_button(self):
        self.click_element(HomePageLocators.yandex_logo)

    @allure.step('Нажать на логотип "Самокат"')
    def click_ya_scooter_logo_button(self):
        self.click_element(HomePageLocators.ya_scooter_logo)
