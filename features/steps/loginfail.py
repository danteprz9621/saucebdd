from behave import *
from selenium import webdriver
from pageObjects.loginpage import *

login = LoginPage()

@then('User must not be able to login')
def step_impl(context):
    login.setDriver(context.driver)
    print(login.getLogErrorMsg().text)
    assert login.getLogErrorMsg().text == "Epic sadface: Sorry, this user has been locked out."

