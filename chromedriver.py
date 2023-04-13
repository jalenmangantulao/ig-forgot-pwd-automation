from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class element_has_forgot_password(object):
    """
    Expectation for checking element that has particular string inside anchor tag
    """

    def __init__(self, element_locator, anchor_text):
        self.element_locator = element_locater # (By.TAG_NAME, "a")
        self.anchor_text = anchor_text
    
    def __call__(self, browser):
        elements = browser.find_elements(*self.element_locator)
        for e in elements:
            if anchor_text == e.accessible_name:
                return e
        else:
            return False

class forgotPwd:
    def __init__(self, repeat_num, username):
        self.repeat_num = repeat_num
        self.username = username # ig username

    def ignore_auto_test_soft_msg(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])

        driver_path = '/Users/jalen/.cache/selenium/chromedriver/win32/111.0.5563.64'
        
    def filter_page_elements(self, browser, tag_type, string_filter):
        # test commit
        web_element_list = []
        web_element_list = browser.find_elements(By.TAG_NAME, tag_type)
        found_element = None
        for element in web_element_list:
            if element.accessible_name == string_filter:
                found_element = element
                break
            else:
                found_element = None
        
        return found_element

    def click_forgot_password(self):
        success_counter = 0
        repeat_this = self.repeat_num
        while repeat_this:
            if repeat_this == success_counter:
                break
            browser = webdriver.Chrome()
            browser.get("https://instagram.com")

            wait = WebDriverWait(browser, 10)
            forgot_pwd_button = wait.until(element_has_forgot_password(By.TAG_NAME, "a"), "Forgot password?")
            # forgot_pwd_button = self.filter_page_elements(browser, "a", "Forgot password?")

            username_form = self.filter_page_elements(browser, "input", "Email, Phone, or Username")
            username_form.send_keys(f"{username}")

            send_login_link_button = self.filter_page_elements(browser, "div", "Send login link")
            send_login_link_button.click()

            success_counter += 1
            
        # click_output = f"Button clicked {button_click_counter} times"
        completion_output = "Success"

        return completion_output

