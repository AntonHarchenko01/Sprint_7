import random
import string
import allure
import requests

from urls import Urls

@allure.step('Генерируем рандомную строку')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

@allure.step('Получаем id курьера')
def get_courier_id(payload):
    courier_response = requests.post(Urls.COURIER_LOGIN, json=payload)
    assert courier_response.status_code == 200
    courier_id = courier_response.json().get('id')
    return courier_id

@allure.step('Удаляем курьера')
def delete_courier(id_courier):
    delete_response = requests.delete(f'{Urls.CREATING_COURIER}/{id_courier}')
    assert delete_response.status_code == 200


@allure.step('регистрация нового курьера возвращает список из логина и пароля')
def register_new_courier_and_return_login_password():
    @allure.step('Генерируем рандомную строку')
    def generate_random_string_courier(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string_courier(10)
    password = generate_random_string_courier(10)
    first_name = generate_random_string_courier(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(Urls.CREATING_COURIER, data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass