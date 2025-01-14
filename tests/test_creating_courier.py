import allure
import requests
from urls import Urls
from helper import generate_random_string, get_courier_id, delete_courier


class TestCreatingCourier:
    @allure.title('Тест проверки успешного создания курьера при заполненных обязательных полях')
    @allure.description('Тест проверяет успешное создание курьера при заполненных полях login и password, получение кода 201 и сообщения {"ok": True}')
    def test_creating_courier_required_fields_filled_courier_created(self):
        payload = {'login': generate_random_string(8), 'password': generate_random_string(8)}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(Urls.CREATING_COURIER, json=payload, headers=headers)
        assert response.status_code == 201
        assert response.json() == {'ok': True}
        id_courier = get_courier_id(payload)
        delete_courier(id_courier)

    @allure.title('Тест проверки, что нельзя создать двух одинаковых курьеров')
    @allure.description('Тест проверки, что при создании двух одинаковых курьеров, получение кода 409 и сообщения "Этот логин уже используется. Попробуйте другой."')
    def test_creating_courier_double_courier_existing_courier(self):
        payload = {'login': generate_random_string(8), 'password': generate_random_string(8)}
        headers = {'Content-Type': 'application/json'}
        requests.post(Urls.CREATING_COURIER, json=payload, headers=headers)
        response = requests.post(Urls.CREATING_COURIER, json=payload, headers=headers)
        assert response.status_code == 409
        response_message = response.text
        assert response_message == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'

    @allure.title('Тест проверки успешного создания курьера при всех заполненных полях')
    @allure.description('Тест проверяет успешное создание курьера при заполненных полях login, password, firstName, получение кода 201 и сообщения {"ok": True}')
    def test_creating_courier_all_fields_filled_courier_created(self):
        payload = {'login': generate_random_string(8), 'password': generate_random_string(8), 'firstName': generate_random_string(8)}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(Urls.CREATING_COURIER, json=payload, headers=headers)
        assert response.status_code == 201
        assert response.json() == {'ok': True}
        id_courier = get_courier_id(payload)
        delete_courier(id_courier)

    @allure.title('Тест проверки, что нельзя создать пользователя без обязательного поля')
    @allure.description('Тест проверяет, что нельзя создать пользователя без обязательного поля пароль, получение кода 400 и сообщения "Недостаточно данных для создания учетной записи"')
    def test_creating_courier_without_password_not_enough_data(self):
        payload = {'login': generate_random_string(8)}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(Urls.CREATING_COURIER, json=payload, headers=headers)
        assert response.status_code == 400
        response_message = response.text
        assert response_message == '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
