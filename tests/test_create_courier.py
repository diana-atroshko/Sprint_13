import pytest
import allure
from methods.courier_methods import CourierMethods


@allure.epic("Тестирование Создание курьера")
class TestCreateCurier:
    def setup_method(self):
        self.courier_methods = CourierMethods()


    @allure.title("Тест на создание нового курьера")
    @allure.description("Проверяет, что курьера можно создать, создавая курьера передаем все обязательные поля, запрос возвращает правильный код ответа, успешный запрос возвращает {ok:true}.")
    def test_create_courier(self, courier_data):
        payload = courier_data
        response = self.courier_methods.create_courier(payload)
        assert response.status_code == 201, 'Курьер не был зарегистрирован - ожидаем статус 201'
        assert response.json() == {
            'ok': True
        }


    @allure.title("Тест на создание дублирующего курьера")
    @allure.description("Проверяет, что попытка создать дубликат курьера возвращает статус 409.")
    def test_create_duplicate_courier(self, courier_data):
        payload = courier_data
        self.courier_methods.create_courier(payload)
        duplicate_response = self.courier_methods.create_courier(payload)
        assert duplicate_response.status_code == 409, 'Ожидаем статус 409 при создании дубликата курьера'


    @pytest.mark.parametrize("payload", [
        {"password": "test_password"},
        {"login": "test_login"},
        {"": "test_login"},
        {"password": "", "login": "test_login"},
        {},
        {"login": "", "password": "test_password"}
    ])
    @allure.title("Тест на создание курьера без обязательных полей")
    @allure.description("Проверяет, что создание курьера без обязательных полей возвращает статус 400.")
    def test_create_courier_missing_fields(self, payload):
        response = self.courier_methods.create_courier(payload)
        assert response.status_code == 400
        assert response.json().get('message') == 'Недостаточно данных для создания учетной записи'


    @allure.title("Тест на создание курьера с уже существующим логином")
    @allure.description("Проверяет, что создание курьера с уже существующим логином возвращает статус 409.")
    def test_create_courier_with_existing_login(self, courier_data):
        payload = courier_data
        self.courier_methods.create_courier(payload)
        payload_with_existing_login = {
            "login": payload["login"],  # Используем логин первого курьера
            "password": "new_password",
            "firstName": "AnotherName"
        }
        response_create_duplicate = self.courier_methods.create_courier(payload_with_existing_login)
        assert response_create_duplicate.status_code == 409, "Ошибка: ожидали статус 409 при создании с существующим логином"



