import allure
import pytest
from methods.courier_methods import CourierMethods

@allure.epic("Тестирование Логина Курьеров")
class TestLoginCourier:
    courier_methods = CourierMethods()

    @pytest.mark.parametrize("payload, expected_status, expected_message", [
        ({"login": "ghghg", "password": "1234"}, 404, "Учетная запись не найдена"),  # Неправильные данные
        ({"login": "", "password": "1234"}, 400, "Недостаточно данных для входа"),  # Отсутствует логин
        ({"login": "ghghg", "password": ""}, 400, "Недостаточно данных для входа"),  # Отсутствует пароль
        ({"login": "", "password": ""}, 400, "Недостаточно данных для входа"),  # Отсутствие полей
    ])
    @allure.title("Тест на вход с некорректными данными")
    @allure.description("Проверяет, что вход с некорректными или отсутствующими данными возвращает ожидаемые ошибки.")
    def test_login_courier_with_invalid_data(self, payload, expected_status, expected_message):
        response = self.courier_methods.login_courier(payload)
        assert response.status_code == expected_status
        assert response.json()["message"] == expected_message

    @allure.title("Тест на успешный вход курьера")
    @allure.description("Создает курьера, затем проверяет, что он может успешно войти в систему и что успешный запрос возвращает id.")
    def test_login_courier_success(self):
        payload = self.courier_methods.generate_courier_data()
        response = self.courier_methods.create_courier(payload)
        assert response.status_code == 201
        response = self.courier_methods.login_courier(payload)

        assert response.status_code == 200
        assert "id" in response.json(), "Ожидали получить id курьера"

    @allure.title("Тест на вход несуществующего курьера")
    @allure.description("Проверяет, что попытка входа с несуществующим логином возвращает статус 404.")
    def test_login_nonexistent_courier(self):
        payload = {"login": "nonexistent_login", "password": "wrong_password"}
        response = self.courier_methods.login_courier(payload)

        assert response.status_code == 404
        assert response.json()['message'] == "Учетная запись не найдена"