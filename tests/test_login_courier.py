import allure
import requests
import data
from helper import register_new_courier_and_return_login_password, delete_courier, get_courier_id, generate_random_string
from urls import Urls


class TestLoginCourier:
    @allure.title('Тест проверки успешной авторизации курьера при заполненных обязательных полей')
    @allure.description('Тест проверяет успешную авторизацию курьера при заполненных полях login, password получение кода 200 и сообщения с id курьера')
    def test_login_courier_required_fields_filled_success_login_courier(self):
        login, password, first_name = register_new_courier_and_return_login_password()
        payload = {'login': login, 'password': password}
        response = requests.post(Urls.COURIER_LOGIN, data=payload)
        assert response.status_code == 200 and 'id' in response.json()
        id_courier = get_courier_id(payload)
        delete_courier(id_courier)

    @allure.title('Тест проверки успешной авторизации курьера при заполнении всех полей')
    @allure.description('Тест проверяет успешную авторизацию курьера при заполненных полях login, password, firstName, получение кода 200 и сообщения с id курьера')
    def test_login_courier_all_fields_filled_success_login_courier(self):
        login, password, first_name = register_new_courier_and_return_login_password()
        payload = {'login': login, 'password': password, 'firstName': first_name}
        response = requests.post(Urls.COURIER_LOGIN, data = payload)
        assert response.status_code == 200 and 'id' in response.json()
        id_courier = get_courier_id(payload)
        delete_courier(id_courier)

    @allure.title('Тест проверки авторизации курьера с неправильно заполненным полем')
    @allure.description('Тест проверяет, что если неправильно заполнить поле password, получим код 404 и сообщение "Учетная запись не найдена"')
    def test_login_courier_wrong_password_account_not_found(self):
        login, password, first_name = register_new_courier_and_return_login_password()
        payload = {'login': login, 'password': '1'}
        response = requests.post(Urls.COURIER_LOGIN, data=payload)
        assert response.status_code == 404
        response_message = response.text
        assert response_message == '{"code":404,"message":"Учетная запись не найдена"}'
        payload = {'login': login, 'password': password, 'firstName': first_name}
        id_courier = get_courier_id(payload)
        delete_courier(id_courier)

    @allure.title('Тест проверки авторизации курьера без ввода пароля')
    @allure.description('Тест проверяет, что курьер без ввода пароля не сможет авторизоваться в системе, получение кода 400 и сообщения "Недостаточно данных для входа"')
    def test_login_courier_not_password_insufficient_data(self):
        payload = {'login': generate_random_string(8), 'password': ''}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(Urls.COURIER_LOGIN, json=payload, headers=headers)
        assert response.status_code == 400
        response_message =  response.text
        assert response_message == '{"code":400,"message":"Недостаточно данных для входа"}'

    @allure.title('Тест проверки авторизации незарегистрированного пользователя')
    @allure.description('Тест проверяет, что курьер не зарегистрированный в системе не может авторизоваться, получение кода 404 и сообщения "Учетная запись не найдена"')
    def test_login_courier_not_registered_courier_account_not_found(self):
        payload = {'login': data.not_exist_login, 'password': data.not_exist_password}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(Urls.COURIER_LOGIN, json=payload, headers=headers)
        assert response.status_code == 404
        response_message = response.text
        assert response_message == '{"code":404,"message":"Учетная запись не найдена"}'


