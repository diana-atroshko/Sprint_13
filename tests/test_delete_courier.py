import allure
import pytest
from methods.courier_methods import CourierMethods

@allure.epic("Тестирование Удаления Курьера")
class TestDeleteCourier:
    courier_methods = CourierMethods()

    @allure.title("Тест на успешное удаление курьера")
    @allure.description("Проверяет, что курьер успешно удаляется и возвращает статус 200.")
    def test_delete_courier_success(self):
        payload = self.courier_methods.generate_courier_data()
        response = self.courier_methods.create_courier(payload)
        assert response.status_code == 201, 'Курьер не был зарегистрирован - ожидаем статус 201'
        assert response.json() == {
            'ok': True
        }
        dlt = self.courier_methods.delete_courier(payload['login'], payload['password'])

        assert dlt.status_code == 200
        assert dlt.json() == {'ok': True}

    @allure.title("Тест на удаление курьера без указания ID")
    @allure.description("Проверяет, что попытка удалить курьера без указания ID возвращает статус 404.")
    def test_delete_courier_no_id(self):
        payload = self.courier_methods.generate_courier_data()
        response = self.courier_methods.create_courier(payload)
        assert response.status_code == 201
        dlt_response = self.courier_methods.delete_courier_with_id(courier_id="")

        assert dlt_response.status_code == 404
        assert dlt_response.json()["message"] == 'Not Found.'

    @allure.title("Тест на удаление курьера с несуществующим ID")
    @allure.description("Проверяет, что удаление курьера с несуществующим ID возвращает статус 404.")
    def test_delete_courier_nonexistent_id(self):
        response = self.courier_methods.delete_courier_with_id(99999)
        assert response.status_code == 404
        assert response.json()['message'] == 'Курьера с таким id нет.'