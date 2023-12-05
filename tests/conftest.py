import pytest
import string
import random
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()

    yield driver
    driver.quit()

@pytest.fixture
def username():
    return "Имя Пользователя"


@pytest.fixture
def user_email():
    return f'Nastya_n_3{random.randint(000,999)}@ya.ru'

@pytest.fixture
def correct_password(length=7):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


@pytest.fixture
def incorrect_password(length=5):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password



