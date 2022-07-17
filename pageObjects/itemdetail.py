from pageObjects.locators import SauceLocators

class ItemDetailPage:

    def setDriver(self, driver):
        self.driver = driver;

    def getItemTitle(self):
        return self.driver.find_element(*SauceLocators.item_title)
