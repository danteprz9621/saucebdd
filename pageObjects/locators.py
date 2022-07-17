from selenium.webdriver.common.by import By


class SauceLocators:
    ##Login Page
    username = (By.XPATH, "//input[@id='user-name']")
    password = (By.XPATH, "//input[@id='password']")
    login_btn = (By.XPATH, "//input[@id='login-button']")
    logerror_msg = (By.XPATH, "//h3[@data-test='error']")

    ##Product Page
    item_name = (By.CLASS_NAME, "inventory_item_name")
    addtocart_btn = (By.CLASS_NAME, "btn_inventory")
    cart_btn = (By.XPATH, "	//a[@class='shopping_cart_link']")
    items_in_cart = (By.XPATH, "//span[@class='shopping_cart_badge']")

    ##Checkout Page
    checkout_btn = (By.XPATH, "//button[@id='checkout']")
    cart_item = (By.CLASS_NAME, "inventory_item_name")
    remove_btn = (By.XPATH, "//button[@id='remove-sauce-labs-bike-light']")

    ##Delivery Page
    first_name = (By.XPATH, "//input[@id='first-name']")
    last_name = (By.XPATH, "//input[@id='last-name']")
    postal_code = (By.XPATH, "//input[@id='postal-code']")
    continue_btn = (By.XPATH, "//input[@id='continue']")

    ##Item Detail Page
    item_title = (By.XPATH, "//div[@class='inventory_details_name large_size']")

    ##Overview Page
    finish_btn = (By.XPATH, "//button[@id='finish']")

    ##Complete Page
    dispatched_text = (By.XPATH, "//div[@class='complete-text']")
