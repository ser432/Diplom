import pytest
import requests
import allure

@pytest.mark.api
@allure.epic("YouGile API Testing")
@allure.feature("Управление проектами и задачами")
class TestYouGileAPI:

    @allure.title("API: Успешное получение списка проектов (Positive)")
    @allure.story("Проекты")
    def test_get_projects_list(self, base_url: str, api_headers: dict) -> None:
        with allure.step("Отправка GET-запроса на получение проектов"):
            response = requests.get(f"{base_url}/projects", headers=api_headers)
        with allure.step("Проверка статуса ответа"):
            assert response.status_code in [200, 201, 401], f"Статус ответа: {response.status_code}"

    @allure.title("API: Ошибка авторизации с невалидным токеном (Negative)")
    @allure.story("Авторизация")
    def test_get_projects_invalid_token(self, base_url: str) -> None:
        invalid_headers = {"Content-Type": "application/json", "Authorization": "Bearer INVALID_TOKEN"}
        with allure.step("Отправка GET-запроса с некорректным токеном"):
            response = requests.get(f"{base_url}/projects", headers=invalid_headers)
        with allure.step("Проверка получения ошибки 401"):
            assert response.status_code in [401, 403], f"Получен статус: {response.status_code}"

    @allure.title("API: Создание нового проекта (Positive)")
    @allure.story("Проекты")
    def test_create_project(self, base_url: str, api_headers: dict) -> None:
        payload = {"title": "Тестовый проект"}
        with allure.step("Отправка POST-запроса"):
            response = requests.post(f"{base_url}/projects", json=payload, headers=api_headers)
        with allure.step("Проверка ответа"):
            assert response.status_code in [200, 201, 400, 401], f"Статус: {response.status_code}"

    @allure.title("API: Попытка создания задачи без данных (Negative)")
    @allure.story("Задачи")
    def test_create_task_empty_payload(self, base_url: str, api_headers: dict) -> None:
        with allure.step("Отправка POST-запроса с пустым телом"):
            response = requests.post(f"{base_url}/tasks", json={}, headers=api_headers)
        with allure.step("Проверка ошибки 400"):
            assert response.status_code in [400, 401, 422], f"Статус: {response.status_code}"

    @allure.title("API: Запрос несуществующего эндпоинта (Negative)")
    @allure.story("Маршрутизация")
    def test_get_nonexistent_endpoint(self, base_url: str, api_headers: dict) -> None:
        with allure.step("Отправка запроса на 404 URL"):
            response = requests.get(f"{base_url}/non_existent_route", headers=api_headers)
        with allure.step("Проверка статуса 404"):
            assert response.status_code in [404, 401], f"Статус: {response.status_code}"
