Автотесты для сервиса https://stellarburgers.nomoreparties.site/ 

data_for_test.py - файл с данными для автотестирования, в том числе содержит логин/пароль для уже зарегистрированного пользователя
conftest.py - фикстуры для формы регистрации, используется генерация пароля и email
test_registration.py - тест проверки регистрации, тест ошибки если пароль некорректный
test_login.py - тесты для формы логина, вызываемого из различных мест
test_navigate_to_account.py - тест перехода в личный кабинет
test_redirect_from_account_to_constructor.py - тесты для проверки перехода в конструктор
test_logout.py - тест кнопки "Выход"
test_redirect_to_constructor_sections.py - тесты проверки перехода в различные разделы конструктора
