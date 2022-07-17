from behave import *
from selenium import webdriver
from pageObjects.loginpage import *

login = LoginPage()

@given('Launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    login.setDriver(context.driver)

@when('Open the Saucedemo page')
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/")

@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context,user,pwd):
    login.getUsernameInput().send_keys(user)
    login.getPasswordInput().send_keys(pwd)
    login.getLoginBtn().click()

@then('User must successfully login')
def step_impl(context):
    assert context.driver.current_url == "https://www.saucedemo.com/inventory.html"

@then('Close browser')
def step_impl(context):
    context.driver.close()
