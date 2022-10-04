import allure
from selene.support.shared import browser
from selene.support import by
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Chesnova")
@allure.feature("Задачи в репозитории")
@allure.story("Неавторизованный пользователь может посмотреть задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps():
    open_main_page()
    search_for_repository('Chesnova/qa_guru_2_8')
    go_to_repository('Chesnova/qa_guru_2_8')
    open_issue_tab()
    should_see_issue_with_number('#1')


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open('https://github.com')


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    s('.header-search-input').click()
    s('.header-search-input').send_keys('Chesnova/qa_guru_2_8')
    s('.header-search-input').submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()