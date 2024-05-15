from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Заголовок страницы заказа
    order_header = [By.XPATH, ".//div[text()='Для кого самокат']"]

    # Данные человека
    name_field = [By.XPATH, ".//input[contains(@placeholder,'* Имя')]"]
    surname_field = [By.XPATH, ".//input[contains(@placeholder,'* Фамилия')]"]
    address_field = [By.XPATH, ".//input[contains(@placeholder,'* Адрес: куда привезти заказ')]"]
    subway_station_button = [By.XPATH, ".//input[contains(@placeholder,'* Станция метро')]"]
    phone_field = [By.XPATH, ".//input[contains(@placeholder,'* Телефон: на него позвонит курьер')]"]

    # Геттер станции метро
    @staticmethod
    def subway_choice_button(station: str):
        return [By.XPATH, f".//div[text()='{station}']/parent::button"]

    # Кнопка "Далее" страницы заказа
    next_button = [By.XPATH, ".//div[@class='Order_NextButton__1_rCA']/button"]

    # Заголовок "Про аренды" в ходе заказа
    about_rent_header = [By.XPATH, ".//div[text()='Про аренду']"]

    # Данные об аренде
    date_field = [By.XPATH, ".//input[contains(@placeholder,'* Когда привезти самокат')]"]
    rent_time_field = [By.XPATH, ".//span[@class='Dropdown-arrow']"]
    rent_time_dropdown_menu = [By.XPATH, ".//div[@class='Dropdown-menu']"]
    rental_time_list = [By.XPATH, ".//div[@class='Dropdown-option']"]
    scooter_color_field = [By.XPATH, ".//input[contains(@placeholder,'* Цвет самоката')]"]
    comment_for_courier_field = [By.XPATH, ".//input[contains(@placeholder,'Комментарий для курьера')]"]
    color_checkboxes = [By.XPATH, ".//div[contains(text(),'Цвет')]/parent::div//input"]

    # Заголовок подтверждения заказа
    want_to_order_header = [By.XPATH, ".//div[text()='Хотите оформить заказ?']"]

    # Кнопки "Да" и "Нет"
    yes_order_button = [By.XPATH, ".//button[text()='Да']"]
    no_order_button = [By.XPATH, ".//button[text()='Нет']"]

    # Кнопки "Назад" и "Заказать" на странице заказа
    go_back_button = [By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Назад']"]
    final_order_button = [By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']"]

    # Заголовок после оформления заказа "Заказ оформлен"
    order_completed_header = [By.XPATH, ".//div[text()='Заказ оформлен']"]

    # Локатор строки с номером заказа
    order_num_str = [By.XPATH, ".//div[contains(text(),'Номер заказа')]"]

    # Кнопка "Посмотреть статус"
    check_status_button = [By.XPATH, ".//button[text()='Посмотреть статус']"]

    # Текстовое поле, содержащее заказ в атрибуте 'value'
    order_num_track_field = [By.CSS_SELECTOR, ".Track_Input__1g7lq"]
