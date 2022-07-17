from behave import *
from pageObjects.productpage import *
from pageObjects.checkoutpage import *

productpage = ProductPage()
checkoutpage = CheckoutPage()
items = []

@then('User adds Sauce Labs Backpack and Sauce Labs Bike Light to cart')
def step_impl(context):
    productpage.setDriver(context.driver)

    addcartbtns = productpage.getCartBtns()

    addcartbtns[0].click()
    addcartbtns[1].click()

    productpage.getCartBtn().click()

@then('User removes last item')
def step_impl(context):
    global items
    checkoutpage.setDriver(context.driver)
    rmvbtn = checkoutpage.getRemoveBtn()
    rmvbtn.click()
    items = checkoutpage.getCartItems()

@then('Last item shouldn\'t appear in cart')
def step_impl(context):

    assert items[0].text == 'Sauce Labs Backpack' and len(items) == 1
