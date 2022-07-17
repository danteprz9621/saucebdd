from behave import *
from pageObjects.checkoutpage import *
from pageObjects.deliverypage import *
from pageObjects.overviewpage import *
from pageObjects.completepage import *

checkoutpage = CheckoutPage()
deliverypage = DeliveryPage()
overpage = OverviewPage()
completepage = CompletePage()


@then('User clicks on checkout button')
def step_impl(context):
    checkoutpage.setDriver(context.driver)
    chkbtn = checkoutpage.getCheckoutBtn()
    chkbtn.click()


@then('User fills checkout information with name "{name}", last name "{lastname}", postal code "{postal}"')
def step_impl(context, name, lastname, postal):
    deliverypage.setDriver(context.driver)
    first = deliverypage.getFirstNameInput()
    last = deliverypage.getLastNameInput()
    post = deliverypage.getPostalCode()
    btn = deliverypage.getContinueBtn()

    first.send_keys(name)
    last.send_keys(lastname)
    post.send_keys(postal)
    btn.click()


@then('User finishes the purchase')
def step_impl(context):
    overpage.setDriver(context.driver)
    continuebtn = overpage.getFinishBtn()
    continuebtn.click()


@then('User sees a success message appears on screen')
def step_impl(context):
    completepage.setDriver(context.driver)
    text = completepage.getDispatchedText().text
    assert text == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
