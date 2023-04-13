from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class element_has_tag(object):
    """
    Expectation for checking element that has particular string inside specified HTML tag
    """

    def __init__(self, element_locator, anchor_text):
        self.element_locator = element_locator # (By.TAG_NAME, "<tag type ex: 'a' or 'input'>")
        self.anchor_text = anchor_text
    
    def __call__(self, browser):
        # element = browser.find_element(*self.element_locator)
        # if self.anchor_text == element.accessible_name:
        #     return element
        # else:
        #     return False

        elements = browser.find_elements(self.element_locator[0], self.element_locator[1])
        # purge list of empty strings to prevent selenium timeout error for large amount of elements returned
        elements = [el for el in elements if len(el.accessible_name) > 1]
        for e in elements:
            if e.accessible_name == self.anchor_text:
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
        username = self.username
        while repeat_this:
            if repeat_this == success_counter:

                break
            browser = webdriver.Chrome()
            browser.get("https://instagram.com")

            wait = WebDriverWait(browser, 10)
            forgot_pwd_button = wait.until(element_has_tag((By.TAG_NAME, "a"), "Forgot password?"))
            forgot_pwd_button.click()
            # forgot_pwd_button = self.filter_page_elements(browser, "a", "Forgot password?")

            wait = WebDriverWait(browser, 10)
            username_form = wait.until(element_has_tag((By.TAG_NAME, "input"), "Email, Phone, or Username"))
            username_form.send_keys(f"{username}")

            # username_form = self.filter_page_elements(browser, "input", "Email, Phone, or Username")
            # username_form.send_keys(f"{username}")

            wait = WebDriverWait(browser, 10)
            send_login_link_button = wait.until(element_has_tag((By.TAG_NAME, "div"), "Send login link"))
            send_login_link_button.click()

            wait = WebDriverWait(browser, 10)
            login_confirm_text = wait.until(element_has_tag((By.TAG_NAME, "h2"), "Confirm it's you to Login"))
            # send_login_link_button = self.filter_page_elements(browser, "div", "Send login link")
            # send_login_link_button.click()

            success_counter += 1
            
        # click_output = f"Button clicked {button_click_counter} times"
        completion_output = f"Successes: {success_counter}"

        return completion_output

