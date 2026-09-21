from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', element)
        self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script('arguments[0].click();', element)

    def set_value(self, locator, text):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', field)
        field.clear()
        field.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def open_url(self, url):
        self.driver.get(url)

    def switch_to_last_window(self):
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def wait_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url(self, condition):
        self.wait.until(lambda driver: condition(driver.current_url))
