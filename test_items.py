from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_tobasket_is_avaliable(browser):
    browser.get(link)
    browser.find_element_by_css_selector(".btn-add-to-basket").click()
    # time.sleep(5)
