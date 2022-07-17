from pageObjects.locators import SauceLocators

class OverviewPage:

    def setDriver(self, driver):
        self.driver = driver;

    def getFinishBtn(self):
        return self.driver.find_element(*SauceLocators.finish_btn)
