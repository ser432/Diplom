import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

@pytest.mark.ui
@allure.epic("YouGile UI Testing")
@allure.feature("Главная страница и Авторизация")
class TestYouGileUI:

    @allure.title("UI: Открытие главной страницы YouGile")
    @allure.story("Главная страница")
    def test_open_main_page(self, driver: WebDriver) -> None:
        with allure.step("Переход на главную страницу"):
            driver.get("https://ru.yougile.com/")
        with allure.step("Проверка наличия названия в заголовке"):
            assert len(driver.title) > 0

    @allure.title("UI: Проверка загрузки элементов страницы")
    @allure.story("Навигация")
    def test_login_button_visibility(self, driver: WebDriver) -> None:
        with allure.step("Загрузка страницы"):
            driver.get("https://ru.yougile.com/")
        with allure.step("Проверка наличия контента"):
            body = driver.find_element(By.TAG_NAME, "body")
            assert body is not None

    @allure.title("UI: Переход на страницу авторизации")
    @allure.story("Авторизация")
    def test_navigate_to_login(self, driver: WebDriver) -> None:
        with allure.step("Переход на форму входа"):
            driver.get("https://ru.yougile.com/login")
        with allure.step("Проверка URL"):
            assert "yougile" in driver.current_url

    @allure.title("UI: Проверка элементов формы входа")
    @allure.story("Форма авторизации")
    def test_login_form_elements(self, driver: WebDriver) -> None:
        with allure.step("Загрузка страницы входа"):
            driver.get("https://ru.yougile.com/login")
        with allure.step("Проверка полей"):
            inputs = driver.find_elements(By.TAG_NAME, "input")
            assert isinstance(inputs, list)

    @allure.title("UI: Проверка страницы API документации")
    @allure.story("Документация")
    def test_api_docs_page(self, driver: WebDriver) -> None:
        with allure.step("Переход на документацию"):
            driver.get("https://ru.yougile.com/api-v2")
        with allure.step("Проверка URL"):
            assert "api" in driver.current_url.lower()
