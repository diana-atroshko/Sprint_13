import allure

from data import ORDER_DATA_1
from methods.order_methods import OrderMethods

@allure.epic("Тестирование Получения Заказа По Номеру")
class TestGetOrder:
    order_methods = OrderMethods()

    @allure.title("Тест на успешное получение заказа по ID")
    @allure.description("Создает заказ и проверяет, что можно успешно получить заказ по его ID.")
    def test_get_order_success(self):
        # Создаем заказ
        response = self.order_methods.create_order(ORDER_DATA_1)
        assert response.status_code == 201
        order_data = response.json()
        order_id = str(order_data["track"])
        getting = self.order_methods.get_order_by_id(order_id)
        assert getting.status_code == 200
        assert 'order' in getting.json()

    @allure.title("Тест на получение заказа без указания ID")
    @allure.description("Проверяет, что запрос без номера заказа возвращает ошибку 400.")
    def test_get_order_missing_order_id(self):
        # Пытаемся получить заказ без ID
        response = self.order_methods.get_order_by_id(order_id="")

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для поиска"

    @allure.title("Тест на получение заказа с невалидным ID")
    @allure.description("Проверяет, что запрос с несуществующим заказом возвращает ошибку 404.")
    def test_get_order_invalid_order_id(self):
        response = self.order_methods.get_order_by_id(order_id=0)

        assert response.status_code == 404
        assert response.json()["message"] == "Заказ не найден"