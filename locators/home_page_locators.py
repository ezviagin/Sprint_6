from selenium.webdriver.common.by import By


class HomePageLocators:
    # Заголовок "Вопросы о важном"
    questions_about_important_title = [By.XPATH, ".//div[text()='Вопросы о важном']"]

    # Кнопка "Заказать" на главной странице
    order_from_home_header_button = [By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']"]
    order_from_home_page_button = [By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']"]

    # "Yandex Самокат" лого
    yandex_logo = [By.XPATH, ".//img[@alt='Yandex']/parent::a[contains(@href, 'yandex')]"]
    ya_scooter_logo = [By.XPATH, ".//a[contains(@class, 'LogoScooter')]"]

    # Список кнопок "Вопросы о важном"
    question_buttons = [By.XPATH, ".//div[@class='accordion__button']"]

    # Геттер пунктов "Вопросы о важном"
    @staticmethod
    def get_question_button(reply):
        return [By.XPATH, f".//div[@class='accordion__panel' and @id='accordion__panel-{reply}']/p"]

    # Кнопка "Да все привыкли"
    accept_cookie_button = [By.XPATH, ".//button[@id='rcc-confirm-button']"]
