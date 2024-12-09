import allure
import pytest
from methods.order_methods import OrderMethods

@allure.epic("Тестирование Получения Списка Заказов")
class TestGetOrders:
    order_methods = OrderMethods()

    @allure.title("Тест на получение списка заказов")
    @allure.description("Проверяет, что запрос на получение списка заказов возвращает статус 200 и корректную структуру ответа.")
    def test_get_orders(self):
        response = self.order_methods.get_orders()

        # Проверка статуса ответа
        assert response.status_code == 200

        response_json = response.json()
        assert "orders" in response_json

        # Проверка, что значение ключа 'orders' является списком
        assert isinstance(response_json["orders"], list)