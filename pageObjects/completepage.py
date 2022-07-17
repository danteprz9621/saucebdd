from pageObjects.locators import SauceLocators

class CompletePage:

    def setDriver(self, driver):
        self.driver = driver;

    def getDispatchedText(self):
        return self.driver.find_element(*SauceLocators.dispatched_text)