import allure
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support import by
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


def test_dynamic_steps():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Неавторизованный пользователь может найти задачу в репозитории")
    allure.dynamic.link("https://github.com", name="Testing")
    with allure.step("Открываем главную страницу"):
        browser.open('https://github.com')

    with allure.step("Ищем репозиторий"):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('Chesnova/qa_guru_2_8')
        s('.header-search-input').submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text('Chesnova/qa_guru_2_8')).click()

    with allure.step("Открываем таб Issues"):
        s('#issues-tab').click()

    with allure.step("Проверяем наличие Issue с номером 1"):
        s(by.partial_text('#1')).should(be.visible)


