import time

import allure

from dmobilaize.Base_test.test_base import Base_test
from selenium.webdriver.common.by import By
from dmobilaize.Locators.login_locator import *


class Login_Page(Base_test):

    def __init__(self):

        self.Login_button = Login_Locator.Login
        self.user_name = Login_Locator.User_name
        self.Password = Login_Locator.password
        self.Login_Button = Login_Locator.login_button
        self.Close_Button = Login_Locator.close_button
        self.x_button = Login_Locator.X_button
        self.na_me = Login_Locator.Name_filled
        self.Pass_Word = Login_Locator.pass_word
        self.Null=Login_Locator.null
        self.Special_character = Login_Locator.special_character
    def common(self):
        super().base_for_web()

    @allure.step
    @allure.description("test_signin")
    @allure.severity(allure.severity_level.CRITICAL)
    def signin(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Login_button).click()

        self.coupon_field = self.driver.find_element(By.XPATH, self.user_name)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.na_me)

        self.coupon_field = self.driver.find_element(By.XPATH, self.Password)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.Pass_Word)

        self.driver.find_element(By.XPATH, self.Login_Button).click()


    @allure.step
    @allure.description("test_invalid_signin")
    @allure.severity(allure.severity_level.CRITICAL)
    def invalid_signin(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Login_button).click()

        self.coupon_field = self.driver.find_element(By.XPATH, self.user_name)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.Null)

        self.coupon_field = self.driver.find_element(By.XPATH, self.Password)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.Null)

        self.driver.find_element(By.XPATH, self.Login_Button).click()


    @allure.step
    @allure.description("test_special_character_signin")
    @allure.severity(allure.severity_level.CRITICAL)
    def special_character_signin(self):

        self.common()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Login_button).click()

        self.coupon_field = self.driver.find_element(By.XPATH, self.user_name)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.Special_character)

        self.coupon_field = self.driver.find_element(By.XPATH, self.Password)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.Special_character)

        self.driver.find_element(By.XPATH, self.Login_Button).click()


    @allure.step
    @allure.description("test_special_character_signin")
    @allure.severity(allure.severity_level.CRITICAL)
    def special_and_Null(self):

        self.common()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Login_button).click()

        self.coupon_field = self.driver.find_element(By.XPATH, self.user_name)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.Null)

        self.coupon_field = self.driver.find_element(By.XPATH, self.Password)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.Null)

        self.driver.find_element(By.XPATH, self.Login_Button).click()


    @allure.step
    @allure.description("test_special_character_signin")
    @allure.severity(allure.severity_level.CRITICAL)
    def special_Null_password(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Login_button).click()

        self.coupon_field = self.driver.find_element(By.XPATH, self.user_name)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.na_me)

        self.coupon_field = self.driver.find_element(By.XPATH, self.Password)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.Null)

        self.driver.find_element(By.XPATH, self.Login_Button).click()


    @allure.step
    @allure.description("test_ close_button")
    @allure.severity(allure.severity_level.CRITICAL)
    def close_button(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.Login_button).click()

        self.driver.find_element(By.XPATH, self.Close_Button).click()


