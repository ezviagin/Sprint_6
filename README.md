# Sprint_5: UI тестирование сайта-сервиса **Яндекс Самокат**

# Описание
UI-тесты функциональности сайта [**Яндекс Самокат**](https://qa-scooter.praktikum-services.ru/) 
в браузере **Mozilla Firefox**

## Стек технологий
- Python 3.11
- PyTest
- Selenium
- Allure
- Firefox и geckodriver

## Запуск тестов

1. Склонировать репозиторий с проектом

2. Перейти в корень проекта

3. Настроить виртуальную среду (virtual environment):
   ```bash
   python -m venv .venv
   ```
4. Запустить virtual environment:
   - Windows
     ```bash
     .venv\Scripts\activate
     ```
   - MacOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
5. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```
6. Установить браузер Mozilla Firefox и geckodriver

7. Указать enviroment path для geckodriver

8. Запуск тестов:
     ```bash
      python -m pytest .\tests\ 
     ```

9. Allure отчеты:
    9.1 Сформировать .json отчёт:
    ``` bash
    python -m pytest .\tests\ --alluredir=allure_results
    ``` 
    9.2 Сформировать .html отчёт:
    ```bash
    allure serve allure_results
    ```
## Проверка функционала (реализованные тесты)

- **Домашняя страница**
  - [x] выпадающий список в разделе "Вопросы о важном"
  - [x] переход на страницу заказа через кнопки главной страницы
    - в header section
    - в home section
  - [x] клик на лого "Yandex" и переход на страницу Дзен
    - в header section
    - в home section
  - [x] клик на лого "Самокат" и переход на домашнюю страницу
    - в header section
    - в home section

- **Страница заказа самоката**
  - [x] полный этап заказа самоката с двумя наборами данных по переходу с главной страницы по клику на кнопку "Заказать"
    - в header secion
    - в home section
  - [x] создание заказа до появления сообщения "Заказ оформлен" по переходу с главной страницы по клику на кнопку "Заказать"
    - в header secion
    - в home section

## Важно
Тесты не будут запускаться с установленным Python интерпреатором версии 3.12, поскольку в нём отсутствует модуль distutils
