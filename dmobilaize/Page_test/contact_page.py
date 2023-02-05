import time

import allure
from selenium.webdriver.common.by import By

from dmobilaize. Base_test.test_base import Base_test
from dmobilaize.Locators.contact_locator import *


class Contact_Page(Base_test):

    def __init__(self):
        self.contact_B = Contact_Locator.contact_button
        self.email_F = Contact_Locator.Email_contact
        self.Name = Contact_Locator.Contact_name
        self.message = Contact_Locator.message_button
        self.close = Contact_Locator.close_buttone
        self.X = Contact_Locator.X_button
        self.send = Contact_Locator.send_message
        self.message_filled = Contact_Locator.message
        self.name_Message = Contact_Locator.name
        self.Email_filled = Contact_Locator.email
        self.invalid_address = Contact_Locator.invalid_email
        self.Null=Contact_Locator.null

    def common(self):
        super().base_for_web()

    @allure.step
    @allure.description("test_Contact_page")
    @allure.severity(allure.severity_level.CRITICAL)
    def contact(self):  # enter valid contact message to the
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.contact_B).click()

        self.email = self.driver.find_element(By.XPATH, self.email_F)
        self.email.clear()
        self.email.send_keys(self.Email_filled)

        self.name = self.driver.find_element(By.XPATH, self.Name)
        self.name.clear()
        self.name.send_keys(self.name_Message)
        self.send = self.driver.find_element(By.XPATH, self.send)
        self.send.clear()
        self.send.send_keys(self.message_filled)
        self.driver.find_element(By.XPATH, self.message).click()

        self.driver.switch_to.alert.accept()


    @allure.step
    @allure.description("test_steps_invalid_email")
    @allure.severity(allure.severity_level.CRITICAL)
    def steps_invalid_email(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.contact_B).click()

        self.coupon_field = self.driver.find_element(By.XPATH, self.email_F)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.invalid_address)

        self.coupon_field = self.driver.find_element(By.XPATH, self.Name)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.name_Message)
        self.coupon_field = self.driver.find_element(By.XPATH, self.send)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.message_filled)
        self.driver.find_element(By.XPATH, self.message).click()

        self.driver.switch_to.alert.accept()


    @allure.step
    @allure.description("test_close_button")
    @allure.severity(allure.severity_level.CRITICAL)
    def close_button(self):  # to check if the close button works properly
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.contact_B).click()

        self.coupon_field = self.driver.find_element(By.XPATH, self.email_F)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.invalid_address)

        self.coupon_field = self.driver.find_element(By.XPATH, self.Name)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.name_Message)

        self.coupon_field = self.driver.find_element(By.XPATH, self.send)
        self.coupon_field.clear()

        self.coupon_field.send_keys(self.message_filled)
        self.driver.find_element(By.XPATH, self.close).click()


    @allure.step
    @allure.description("test_X_button")
    @allure.severity(allure.severity_level.CRITICAL)
    def X_button(self):  # verify that the "X" button woks properly
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.contact_B).click()

        self.coupon_field = self.driver.find_element(By.XPATH, self.email_F)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.invalid_address)

        self.coupon_field = self.driver.find_element(By.XPATH, self.Name)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.name_Message)

        self.coupon_field = self.driver.find_element(By.XPATH, self.send)
        self.coupon_field.clear()

        self.coupon_field.send_keys(self.message_filled)

        self.driver.find_element(By.XPATH, self.X).click()

        self.driver.close()

    @allure.step
    @allure.description("test_close_button")
    @allure.severity(allure.severity_level.CRITICAL)
    def Test_contact_NULL(self):  # to check if the close button works properly
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.contact_B).click()

        self.coupon_field = self.driver.find_element(By.XPATH, self.email_F)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.Null)

        self.coupon_field = self.driver.find_element(By.XPATH, self.Name)
        self.coupon_field.clear()
        self.coupon_field.send_keys(self.Null)

        self.coupon_field = self.driver.find_element(By.XPATH, self.send)
        self.coupon_field.clear()

        self.coupon_field.send_keys(self.Null)
        self.driver.find_element(By.XPATH, self.close).click()
