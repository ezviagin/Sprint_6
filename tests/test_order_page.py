import allure
import pytest

from conftest import driver
from locators.order_page_locators import OrderPageLocators
from locators.home_page_locators import HomePageLocators
from pages.order_page import YaScooterOrderPage
from utils.test_data import YaScooterOrderData as order
import utils.urls as url


@allure.epic('Тестирование интерфейса домашней страницы "Оформление заказа" сервиса "Yandex Самокат"')
@allure.parent_suite('Оформление заказа')
@allure.suite('Order')
class TestOrderPage:
    @allure.feature('Заказ самоката')
    @allure.story('При нажатии на любую кнопку "Заказать" с домашней страницы открывается форма заказа')
    @allure.title('Заказ самоката до получения номера заказа')
    @allure.description('Проверка корректного оформления заказа с использованием двух наборов данных. Тест '
                        'запускается при нажатии обеих кнопок "Заказать" на домашней странице')
    @pytest.mark.parametrize('order_button, data_set',
                             [
                                 (HomePageLocators.order_from_home_header_button, 'data_set_1'),
                                 (HomePageLocators.order_from_home_header_button, 'data_set_2'),
                                 (HomePageLocators.order_from_home_page_button, 'data_set_1'),
                                 (HomePageLocators.order_from_home_page_button, 'data_set_2'),
                             ])
    def test_create_complete_order_header_and_page_order_buttons_positive(self, driver, order_button, data_set):
        page = YaScooterOrderPage(driver)
        page.navigate(url.YA_SCOOTER_HOME_PAGE)
        page.accept_cookies()

        page.scroll_to_element(order_button)
        page.click_element(order_button)
        page.fill_user_order_data(order.data_sets[data_set])
        page.click_next_button()
        assert page.element_is_visible(OrderPageLocators.about_rent_header).text == "Про аренду"

        page.fill_rent_data(order.data_sets[data_set])
        page.click_final_order_button()
        assert "Хотите оформить заказ" in page.element_is_visible(OrderPageLocators.want_to_order_header).text

        page.click_yes_order_button()
        assert "Заказ оформлен" in page.element_is_visible(OrderPageLocators.order_completed_header).text

        actual_order_num = page.get_order_number()
        page.click_check_status_button()

        displayed_order_num = page.get_order_number_after_order_completed()
        current_url = page.current_url()

        assert actual_order_num == displayed_order_num
        assert url.YA_SCOOTER_ORDER_STATUS_PAGE in current_url
        assert str(displayed_order_num) in current_url

        page.click_element(HomePageLocators.ya_scooter_logo)
        page.delete_all_cookies()

        assert page.current_url() == url.YA_SCOOTER_HOME_PAGE

    @allure.feature('Заказ самоката')
    @allure.story('При нажатии на любую кнопку "Заказать" с домашней страницы открывается форма заказа')
    @allure.title('Заказ самоката до перехода к заголовку "Про аренду"')
    @allure.description('Проверка корректного оформления заказа с использованием одного набора данных. Тест '
                        'запускается при нажатии обеих кнопок "Заказать" на домашней странице')
    @pytest.mark.parametrize('order_button',
                             [
                                HomePageLocators.order_from_home_header_button,
                                HomePageLocators.order_from_home_page_button,
                             ])
    def test_create_order_until_order_complete_positive(self, driver, order_button):
        page = YaScooterOrderPage(driver)
        page.navigate(url.YA_SCOOTER_HOME_PAGE)
        page.accept_cookies()

        page.scroll_to_element(order_button)
        page.click_element(order_button)
        page.fill_user_order_data(order.data_sets['data_set_1'])
        page.click_next_button()
        assert page.element_is_visible(OrderPageLocators.about_rent_header).text == "Про аренду"

        page.fill_rent_data(order.data_sets['data_set_1'])
        page.click_final_order_button()
        assert "Хотите оформить заказ" in page.element_is_visible(OrderPageLocators.want_to_order_header).text

        page.click_yes_order_button()
        page.delete_all_cookies()

        assert "Заказ оформлен" in page.element_is_visible(OrderPageLocators.order_completed_header).text
