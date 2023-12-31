# MARM_4 - Тестирование UI

## Предварительные требования
- Для выполнения тестов необходим установленный браузер Mozilla Firefox.
- Для настройки и запуска проекта требуется Python и интегрированная среда разработки (IDE).
- Для работы необходимо установить фреймворки Selenium и Allure.



## Описание

Данный проект представляет собой автоматизацию тестирования функциональности МАРМ-4 ККТ с использованием фреймворка pytest и библиотек
- `selenium`
- `faker` данная библиотека использовалась для генерации `имен`, `email` пользователей, а также для генерации паролей для регистрации
- `random` 
- В проекте составлен отчет в `allure` 
- Проект выполнен с использованием методологии `Page Object Modal`(POM)


## Запуск тестов на ПК

1. Откройте терминал или командную строку.
2. Перейдите в директорию проекта.
3. Выполните следующую команду для запуска тестов:

`pytest --alluredir=./allure_results`

## Отчёт о тестировании

После выполнения тестов можно сгенерировать отчёт Allure, следуя указанным шагам:
1. Откройте терминал или командную строку.
2. Перейдите в директорию проекта.
3. Выполните следующую команду для генерации отчёта Allure:

`allure serve ./allure_results`

Сгенерированный отчёт откроется в вашем основном веб-браузере и будет содержать подробную информацию о выполнении тестов.


## Запуск тестов на виртуальной машине

1. Откройте терминал или командную строку.
2. Перейдите в директорию проекта.
3. Выполните следующую команду для запуска тестов:

`pytest --alluredir=./allure_results`

## Генерация отчета и запуск сервера для просмотра

После выполнения тестов можно сгенерировать отчёт Allure, следуя указанным шагам:
1. Откройте терминал или командную строку.
2. Перейдите в директорию проекта.
3. Выполните следующую команду для генерации отчёта Allure:

`allure serve ./allure_results`

Запуск тестирования и сервера для просмотра отчета реализован посредством cron - ежедневно в 