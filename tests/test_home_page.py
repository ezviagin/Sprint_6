import allure
import pytest
from selenium import webdriver


from locators.home_page_locators import HomePageLocators
from locators.order_page_locators import OrderPageLocators
from pages.home_page import YaScooterHomePage
from utils.test_data import QuestionsAboutImportantData as expected
import utils.urls as url


@allure.epic('Тестирование интерфейса домашней страницы "Yandex Самокат"')
@allure.parent_suite('Домашняя страница')
@allure.suite('Home')
class TestHomePage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.feature('Нажатие на кнопки "Вопросы о важном"')
    @allure.story('При нажатии на вопрос в разделе "Вопросы о важном" выпадает текст с ответом')
    @allure.title('Выпадение ответа при нажатии')
    @allure.description('Проверка нажатия всех восьми (8) кнопок с вопросами и получения соответствующего ответа')
    @pytest.mark.parametrize(
        "question_id, expected_reply",
        [
            (0, expected.text0),
            (1, expected.text1),
            (2, expected.text2),
            (3, expected.text3),
            (4, expected.text4),
            (5, expected.text5),
            (6, expected.text6),
            (7, expected.text7),
        ]
    )
    def test_click_on_all_questions_about_important(self, question_id, expected_reply):
        page = YaScooterHomePage(self.driver)
        page.navigate(url.YA_SCOOTER_HOME_PAGE)

        page.scroll_to_question_about_important_section()
        page.click_question_buttons(question_id)
        res = page.find_element(HomePageLocators.get_question_button(question_id))

        assert res.is_displayed() and res.text == expected_reply

    @allure.feature('Переход на страницу Заказа с домашней страницы')
    @allure.story('При нажатии на кнопку "Заказать" осуществляется переход на страницу заказа')
    @allure.title('Переход на страницу "Оформление заказа"')
    @allure.description('Проверка коррекнтного перехода на страницу "Оформление заказа" по кнопке "Заказать" из header '
                        'домашней страницы и блока "Как это работает"')
    @pytest.mark.parametrize('order_button',
                             [
                                 HomePageLocators.order_from_home_header_button,
                                 HomePageLocators.order_from_home_page_button
                             ]
                             )
    def test_click_on_order_buttons_from_header_and_home_sections(self, order_button):
        page = YaScooterHomePage(self.driver)
        page.navigate(url.YA_SCOOTER_HOME_PAGE)

        page.scroll_to_element(order_button)
        page.click_element(order_button)
        page.element_is_visible(OrderPageLocators.order_header)

        assert page.current_url() == url.YA_SCOOTER_ORDER_PAGE

    @allure.feature('Нажатие на лого "Yandex" с домашней страницы')
    @allure.story('При нажатии на лого "Yandex" открывается новая вкладка dzen.ru')
    @allure.title('Открытие вкладки /order')
    @allure.description('Проверка корректных открытия и перехода на страницу dzen.ru после клика на логотип Yandex в '
                        'шапке главной страницы')
    def test_click_on_yandex_logo_from_home_page(self):
        page = YaScooterHomePage(self.driver)
        page.navigate(url.YA_SCOOTER_HOME_PAGE)

        page.click_yandex_logo_button()
        page.switch_to(1)
        page.wait_for_url()

        assert url.DZEN_HOME_PAGE in page.current_url()

    @allure.feature('Нажатие на лого "Yandex" со страницы "Оформление заказа"')
    @allure.story('При нажатии на лого "Yandex" открывается новая вкладка dzen.ru')
    @allure.title('Открытие вкладки /order')
    @allure.description('Проверка корректных открытия и перехода на страницу dzen.ru после клика на логотип Yandex в '
                        'шапке страницы "Оформление заказа"')
    def test_click_on_yandex_logo_from_home_page(self):
        page = YaScooterHomePage(self.driver)
        page.navigate(url.YA_SCOOTER_ORDER_PAGE)

        page.click_yandex_logo_button()
        page.switch_to(1)
        page.wait_for_url()

        assert url.DZEN_HOME_PAGE in page.current_url()

    @allure.feature('Нажатие на лого "Самокат" с домашней страницы"')
    @allure.story('При нажатии на лого "Самокат" URL дрес не меняется')
    @allure.title('Остаемся на домашней странице')
    @allure.description('Проверка корректных открытия и перехода на домашнюю страницу после клика на логотип Самокат в '
                        'шапке домашней страницы')
    def test_click_on_ya_scooter_logo_from_home_page(self):
        page = YaScooterHomePage(self.driver)
        page.navigate(url.YA_SCOOTER_HOME_PAGE)
        page.click_ya_scooter_logo_button()

        assert url.YA_SCOOTER_HOME_PAGE == page.current_url()

    @allure.feature('Нажатие на лого "Самокат" со страницы "Оформление заказа"')
    @allure.story('При нажатии на лого "Самокат" открывается домашняя страница')
    @allure.title('Открытие домашней страницы')
    @allure.description('Проверка корректных открытия и перехода на страницу dzen.ru после клика на логотип "Самокат" в'
                        'шапке страницы "Оформление заказа"')
    def test_click_on_ya_scooter_logo_from_order_page(self):
        page = YaScooterHomePage(self.driver)
        page.navigate(url.YA_SCOOTER_ORDER_PAGE)
        page.click_ya_scooter_logo_button()

        assert url.YA_SCOOTER_HOME_PAGE == page.current_url()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
