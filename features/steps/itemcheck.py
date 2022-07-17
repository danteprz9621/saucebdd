from behave import *
from pageObjects.productpage import *
from pageObjects.checkoutpage import *
from pageObjects.itemdetail import *

productpage = ProductPage()
checkoutpage = CheckoutPage()
itempage = ItemDetailPage()


@then('User adds Sauce Labs Backpack to cart')
def step_impl(context):
    productpage.setDriver(context.driver)

    addcartbtns = productpage.getCartBtns()

    addcartbtns[0].click()

    productpage.getCartBtn().click()

@then('User clicks on item name')
def step_impl(context):
    checkoutpage.setDriver(context.driver)
    item = checkoutpage.getCartItems()
    item[0].click()

@then('User sees item detail')
def step_impl(context):
    itempage.setDriver(context.driver)
    item = itempage.getItemTitle().text

    assert item == 'Sauce Labs Backpack'