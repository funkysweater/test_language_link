import pytest
import time


def test_language_link(browser, language):
    link = "http://selenium1py.pythonanywhere.com/{}/catalogue/coders-at-work_207/".format(language)
    browser.get(link)
    # time.sleep(5)
    browser.find_element_by_css_selector(".btn-add-to-basket").click()
    # time.sleep(5)
