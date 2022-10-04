from selene.support.conditions import be
from selene.support.shared import browser
from selene.support import by
from selene.support.shared.jquery_style import s


def test_github():
    browser.open('https://github.com')

    s('.header-search-input').click()
    s('.header-search-input').send_keys('Chesnova/qa_guru_2_8')
    s('.header-search-input').submit()

    s(by.link_text('Chesnova/qa_guru_2_8')).click()

    s('#issues-tab').click()

    s(by.partial_text('#1')).should(be.visible)