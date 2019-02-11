from selenium import webdriver
import time
import pytest
import allure
import moment
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

        time.sleep(3)

    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_admin()
            homepage.click_logout()
            x = driver.title
            assert x == "Dalet Brio Web PortalAAA"

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currTime = x = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName, attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/obulgakova/PycharmProjects/AutoWork_1/screenshots/" + screenshotName + ".png")
            raise

        except:
            print("There was am exception")

        else:
            print("No exception occured")

        finally:
            print("I am inside finally block")