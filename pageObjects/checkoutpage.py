from pageObjects.locators import SauceLocators

class CheckoutPage:

    def setDriver(self, driver):
        self.driver = driver;

    def getCheckoutBtn(self):
        return self.driver.find_element(*SauceLocators.checkout_btn)

    def getCartItems(self):
        return self.driver.find_elements(*SauceLocators.cart_item)

    def getRemoveBtn(self):
        return self.driver.find_element(*SauceLocators.remove_btn)