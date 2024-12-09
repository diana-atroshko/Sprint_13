import random
import string

import allure
import requests

from data import COURIER_REGISTRATION_URL, COURIER_LOGIN_URL


class CourierMethods:

    @allure.step("Генерируем данные для регистрации курьера")
    def generate_courier_data(self):
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string


        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return payload

    @allure.step("Создаем курьера")
    def create_courier(self, payload):
        return requests.post(COURIER_REGISTRATION_URL, json=payload)

    @allure.step("Логинимся как курьер")
    def login_courier(self, payload):
        return requests.post(COURIER_LOGIN_URL, json=payload)

    @allure.step("Получаем ID курьера")
    def get_courier_id(self, login, password):
        login_payload = {
            "login": login,
            "password": password
                        }
        login_response = self.login_courier(login_payload)
        return login_response.json().get("id")

    @allure.step("Удаляем курьера через логин и пароль")
    def delete_courier(self, login, password):
        courier_id = self.get_courier_id(login, password)
        response = requests.delete(f'{COURIER_REGISTRATION_URL}/{courier_id}')
        return response

    @allure.step("Удаляем курьера с ID")
    def delete_courier_with_id(self, courier_id):
        response = requests.delete(f'{COURIER_REGISTRATION_URL}/{courier_id}')
        return response
