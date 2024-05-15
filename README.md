# Sprint_5: UI тестирование сайта-сервиса **Яндекс Самокат**

# Описание
UI-тесты функциональности сайта [**Яндекс Самокат**](https://qa-scooter.praktikum-services.ru/) 
в браузере **Mozilla Firefox**

## Стек технологий
- Python 3.11+
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
   - в один поток:
     ```bash
     pytest -v tests
     ```
   - в несколько потоков (например, `4`):
     ```bash
     pytest -n 4 -v tests
     ```
9. Allure отчеты:
    9.1 Сформировать .json отчёт:
    ```pytest <tests> --alluredir=allure_results
    ``` 
    9.2 Сформировать .html отчёт:
    ```pytest <tests> --alluredir=allure_results
    ```
         - 
## Проверка функционала (реализованные тесты)

- **Регистрация**
  - [x] успешная
  - [x] неуспешная (пароль менее 6 символов)


- **Вход**
  - [x] по кнопке «Войти в аккаунт» на главной
  - [x] через кнопку «Личный кабинет»
  - [x] через кнопку в форме регистрации
  - [x] через кнопку в форме восстановления пароля


- **Переход в личный кабинет**
  - [x] по клику на «Личный кабинет»


- **Выход из аккаунта**
  - [x] по кнопке «Выйти» в личном кабинете


- **Переход из личного кабинета в «Конструктор»**
  - [x] по клику на «Конструктор»
  - [x] на логотип Stellar Burgers
  - 
- **Переходы к разделам Конструктор бургеров**
  - [x] «Булки»
  - [x] «Соусы»
  - [x] «Начинки»
