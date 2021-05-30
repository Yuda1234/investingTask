
class SeleniumElementsTools:

    def __init__(self, driver, wait_element):
        self.driver = driver
        self.wait = wait_element

    def get_text_from_element(self, selector, driver=None, timeout=30):
        driver = driver or self.driver
        element_text = self.wait.wait_for_element_to_be_present(selector=selector, driver=driver, timeout=timeout).text
        return element_text
