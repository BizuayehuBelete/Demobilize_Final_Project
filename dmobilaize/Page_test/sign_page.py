import time
import allure
from dmobilaize.Base_test.test_base import Base_test
from selenium.webdriver.common.by import By
from dmobilaize.Locators.sign_up_locator import *


class Signin_Page(Base_test):

    def __init__(self):

        self.Signin_Button = sign_up_Locator.signup_button
        self.Signup_user = sign_up_Locator.signin_username
        self.signup_password = sign_up_Locator.signin_password
        self.Name = sign_up_Locator.name
        self.Password = sign_up_Locator.password
        self.sign_UP_button = sign_up_Locator.sign_up_button
        self.Close = sign_up_Locator.close_button
        self.Special_character = sign_up_Locator.special_character
        self.null = sign_up_Locator.Null
        self.Invalid_password=sign_up_Locator.invalid_password
        self.X=sign_up_Locator.x

    def common(self):
        super().base_for_web()

    @allure.step
    @allure.description("test_ sign_up_test")
    @allure.severity(allure.severity_level.CRITICAL)
    def sign_up_test(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Signin_Button).click()

        self.coupon_field = self.driver.find_element(By.XPATH, self.Signup_user)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.Name)

        self.coupon_field = self.driver.find_element(By.XPATH, self.signup_password)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.Password)

        self.driver.find_element(By.XPATH, self.sign_UP_button).click()


    @allure.description("test_ sign_up_test_with_special_character")
    @allure.severity(allure.severity_level.CRITICAL)
    def sign_up_test_with_special_character(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Signin_Button).click()

        self.coupon_field = self.driver.find_element(By.XPATH, self.Signup_user)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.Special_character)

        self.coupon_field = self.driver.find_element(By.XPATH, self.signup_password)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.Special_character)

        self.driver.find_element(By.XPATH, self.sign_UP_button).click()


    @allure.step
    @allure.description("test_sign_up_test_with_Null")
    @allure.severity(allure.severity_level.CRITICAL)
    def sign_up_test_with_Null(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Signin_Button).click()

        self.coupon_field = self.driver.find_element(By.XPATH, self.Signup_user)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.null)

        self.coupon_field = self.driver.find_element(By.XPATH, self.signup_password)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.null)

        self.driver.find_element(By.XPATH, self.sign_UP_button).click()


    @allure.step
    @allure.description("test_test_short_password")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_short_password(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Signin_Button).click()

        self.coupon_field = self.driver.find_element(By.XPATH, self.Signup_user)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.Name)

        self.coupon_field = self.driver.find_element(By.XPATH, self.signup_password)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.Invalid_password)

        self.driver.find_element(By.XPATH, self.sign_UP_button).click()


    @allure.step
    @allure.description("test_sign_up_test_close")
    @allure.severity(allure.severity_level.CRITICAL)
    def sign_up_test_close(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Signin_Button).click()

        self.driver.find_element(By.XPATH, self.Close).click()


    @allure.step
    @allure.description("test_sign_up_X_button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sign_up_X_button(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Signin_Button).click()

        self.driver.find_element(By.XPATH, self.X).click()


    @allure.step
    @allure.description("test_test_name_null")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_name_null(self):#test when only name null
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Signin_Button).click()

        self.coupon_field = self.driver.find_element(By.XPATH, self.Signup_user)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.null)

        self.coupon_field = self.driver.find_element(By.XPATH, self.signup_password)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.Password)

        self.driver.find_element(By.XPATH, self.sign_UP_button).click()


    @allure.step
    @allure.description("test_test_name_null")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_password_null(self):#test when only password null
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Signin_Button).click()

        self.coupon_field = self.driver.find_element(By.XPATH, self.Signup_user)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.Name)

        self.coupon_field = self.driver.find_element(By.XPATH, self.signup_password)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.null)

        self.driver.find_element(By.XPATH, self.sign_UP_button).click()


    @allure.step
    @allure.description("test_name_specilcharacter")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_name_specilcharacter(self):#test when only name specilcharacter
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Signin_Button).click()

        self.coupon_field = self.driver.find_element(By.XPATH, self.Signup_user)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.Special_character)

        self.coupon_field = self.driver.find_element(By.XPATH, self.signup_password)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.Password)

        self.driver.find_element(By.XPATH, self.sign_UP_button).click()


