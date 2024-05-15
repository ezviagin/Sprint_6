import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
import re


class YaScooterOrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ввод имени')
    def input_name(self, name: str):
        self.enter_text(OrderPageLocators.name_field, name)

    @allure.step('Ввод фамилии')
    def input_surname(self, surname: str):
        self.enter_text(OrderPageLocators.surname_field, surname)

    @allure.step('Ввод адреса')
    def input_address(self, address: str):
        self.enter_text(OrderPageLocators.address_field, address)

    @allure.step('Ввод станции метро')
    def input_subway_station(self, station: str):
        self.find_element(OrderPageLocators.subway_station_button).click()
        return self.find_element(OrderPageLocators.subway_choice_button(station)).click()

    @allure.step('Ввод номера телефона')
    def input_phone_number(self, phone: str):
        self.enter_text(OrderPageLocators.phone_field, phone)

    @allure.step('Ввод даты')
    def input_date(self, date: str):
        self.enter_text(OrderPageLocators.date_field, date)
        self.press_enter_button(OrderPageLocators.date_field)

    @allure.step('Ввод времени аренды (в сутках)')
    def input_rent_time(self, rent_time: int):
        self.click_element(OrderPageLocators.rent_time_field)
        self.element_is_visible(OrderPageLocators.rent_time_dropdown_menu)
        self.find_elements(OrderPageLocators.rental_time_list)[rent_time].click()

    @allure.step('Ввод цвета')
    def input_color(self, color: int):
        self.find_elements(OrderPageLocators.color_checkboxes)[color].click()

    @allure.step('Ввод комментария для курьера')
    def input_comment_for_courier(self, comment: str):
        self.enter_text(OrderPageLocators.comment_for_courier_field, comment)

    @allure.step('Заполнить данные заказа')
    def fill_user_order_data(self, data_set: dict):
        self.input_name(data_set['name'])
        self.input_surname(data_set['surname'])
        self.input_address(data_set['address'])
        self.input_subway_station(data_set['station'])
        self.input_phone_number(data_set['phone_number'])

    @allure.step('Нажать кнопку "Далее" в процессе оформления заказа')
    def click_next_button(self):
        self.scroll_to_element(OrderPageLocators.next_button)
        self.click_element(OrderPageLocators.next_button)

    @allure.step('Заполнить данные об аренде')
    def fill_rent_data(self, data_set: dict):
        self.input_date(data_set['date'])
        self.input_rent_time(data_set['rent_time'])
        for color in data_set['color']:
            self.input_color(color)
        self.input_comment_for_courier(data_set['comment_for_courier'])

    @allure.step('Нажать кнопку "Заказать"')
    def click_final_order_button(self):
        self.click_element(OrderPageLocators.final_order_button)

    @allure.step('Нажать кнопку "Да" в процессе оформления заказа')
    def click_yes_order_button(self):
        self.click_element(OrderPageLocators.yes_order_button)

    @allure.step('Получить номер заказа')
    def get_order_number(self) -> int:
        order_str = self.find_element(OrderPageLocators.order_num_str).text
        match = re.search(r'\d+', order_str)
        if match:
            return int(match.group())
        else:
            return -1

    @allure.step('Нажать кнопку "Посмотреть статус" после оформления заказа')
    def click_check_status_button(self):
        self.click_element(OrderPageLocators.check_status_button)

    @allure.step('Получить номер заказа после оформления')
    def get_order_number_after_order_completed(self) -> int:
        return int(self.find_element(OrderPageLocators.order_num_track_field).get_attribute('value'))
