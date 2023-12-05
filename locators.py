
reg_name = './/label[text()="Имя"]/following-sibling::input' #форма регистрации, поле "Имя"
email = './/label[text()="Email"]/following-sibling::input' #логин/регистрация, поле Email
password = './/label[text()="Пароль"]/following-sibling::input' #логин/регистрация, поле Пароль
reg_button = ".//button[text()='Зарегистрироваться']" # регистрация: кнопка регистрации
login_button = './/button[text()="Войти"]' # логин, кнопка "Войти"
enter_title = './/h2[text()="Вход"]' #логин, тайтл "Вход"
login_to_account = ".//button[text()='Войти в аккаунт']"  # главная, кнопка "Войти в аккаунт"
error_pass = '.input__error' # логин, "Некорректный пароль"

burger_title = './/h1[text()="Соберите бургер"]' #главная, название блока «Соберите бургер»
to_account = ".//*[@href='/account']" # главная, кнопка "Личный кабинет"
make_order = './/button[text()="Оформить заказ"]' #  главная, кнопка "Оформить заказ" для зарегистрированного пользователя

orders_history = './/a[text()="История заказов"]' # ЛК, блок "История заказов"
logout_button = './/button[text()="Выход"]' # ЛК, кнопка выхода
reg_from_login = 'a[href="/register"]' #страницы логина: кнопка "Зарегистрироваться"
login_from_reg_and_forgot = 'a[href="/login"]' # кнопка "Войти" на странице регистрации И на странице восстановления пароля

#Разделы на главной
sauces_tab = './/span[text()="Соусы"]' # раздел "Соусы" на главной
sauces = '//span[text()="Соусы"]/parent::div' # div раздела Соусы, в котором хранятся классы
fills_tab = './/span[text()="Начинки"]' # раздел "Начинки" на главной
fills = '//span[text()="Начинки"]/parent::div' # div раздела Начинки, в котором хранятся классы
bread_tab = './/span[text()="Булки"]' #раздел "Булки" на главной
bread = '//span[text()="Булки"]/parent::div' #  div раздела Булки, в котором хранятся классы
burger_assemble = ".BurgerIngredients_ingredients__1N8v2" # главная, весь блок "Соберите бургер" с табами

constructor_button = './/p[text()="Конструктор"]' # шапка, кнопка "Конструктор"
main_logo = 'div.AppHeader_header__logo__2D0X2' # шапка, иконка и кнопка с лого
drag_the_bread = "ul.BurgerConstructor_basket__list__l9dp_" # блок с перетягиванием булочек на главной странице
