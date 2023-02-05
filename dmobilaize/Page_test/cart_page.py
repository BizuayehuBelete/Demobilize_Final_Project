import time

import allure
from selenium.webdriver.common.by import By

from dmobilaize.Base_test.test_base import Base_test
from dmobilaize.Locators.Cart_Locatore import Cart_Page_Locatore


class Cart_page(Base_test):

    def __init__(self):
        self.button = Cart_Page_Locatore.cart_button

        self.order = Cart_Page_Locatore.click_place_order_button

        self.Xpath_name = Cart_Page_Locatore.path_name

        self.Name=Cart_Page_Locatore.name

        self.country = Cart_Page_Locatore.country_name

        self.Country= Cart_Page_Locatore.Cuntry

        self.city = Cart_Page_Locatore.city_name

        self.City=Cart_Page_Locatore.City

        self.card = Cart_Page_Locatore. cridit_carde

        self.Card_no=Cart_Page_Locatore.Card

        self.month = Cart_Page_Locatore.month

        self.MONTH= Cart_Page_Locatore.mo_nth

        self.year = Cart_Page_Locatore.year

        self.YEAR=Cart_Page_Locatore.ye_ar

        self.purchase = Cart_Page_Locatore.purchase

        self.close = Cart_Page_Locatore. close_button
        self.Null=Cart_Page_Locatore.null
        self.special_character=Cart_Page_Locatore.special_character
        self.X=Cart_Page_Locatore.x

    def common(self):
        super().base_for_web()

    @allure.step
    @allure.description("cart valid placeholder address")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_page(self):
        self.common()
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.order).click()

        self.driver.find_element(By.XPATH, self.Xpath_name).send_keys(self.Name)

        self.driver.find_element(By.XPATH, self.country).send_keys(self.Country)

        self.driver.find_element(By.XPATH, self.city).send_keys(self.City)

        self.driver.find_element(By.XPATH, self.card).send_keys(self.Card_no)

        self.driver.find_element(By.XPATH, self.month).send_keys(self.MONTH)

        self.driver.find_element(By.XPATH, self.year).send_keys(self.YEAR)

        self.driver.find_element(By.XPATH, self.purchase).click()

        self.driver.find_element(By.XPATH, self.close).click()


    @allure.step
    @allure.description("cart invalid placeholder address")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_page_invalid(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.button).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.order).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Xpath_name).send_keys(self.Null)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.country).send_keys(self.Null)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.city).send_keys(self.Null)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.card).send_keys(self.Null)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.month).send_keys(self.Null)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.year).send_keys(self.Null)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.purchase).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.close).click()
        time.sleep(3)

    @allure.step
    @allure.description("cart invalid placeholder address")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_page_secial_character(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.order).click()

        self.driver.find_element(By.XPATH, self.Xpath_name).send_keys(self.special_character)

        self.driver.find_element(By.XPATH, self.country).send_keys(self.Country)

        self.driver.find_element(By.XPATH, self.city).send_keys(self.City)

        self.driver.find_element(By.XPATH, self.card).send_keys(self.special_character)

        self.driver.find_element(By.XPATH, self.month).send_keys(self.Null)

        self.driver.find_element(By.XPATH, self.year).send_keys(self.YEAR)

        self.driver.find_element(By.XPATH, self.purchase).click()

        self.driver.find_element(By.XPATH, self.close).click()


    @allure.step
    @allure.description("cart invalid placeholder address")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_page_secial_characterand_Null(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.order).click()

        self.driver.find_element(By.XPATH, self.Xpath_name).send_keys(self.Name)

        self.driver.find_element(By.XPATH, self.country).send_keys(self.Country)

        self.driver.find_element(By.XPATH, self.city).send_keys(self.City)

        self.driver.find_element(By.XPATH, self.card).send_keys(self.special_character)

        self.driver.find_element(By.XPATH, self.month).send_keys(self.Null)

        self.driver.find_element(By.XPATH, self.year).send_keys(self.Null)

        self.driver.find_element(By.XPATH, self.purchase).click()

        self.driver.find_element(By.XPATH, self.close).click()


    @allure.step
    @allure.description("cart invalid placeholder address")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_page_secial_close(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.order).click()

        self.driver.find_element(By.XPATH, self.Xpath_name).send_keys(self.Name)

        self.driver.find_element(By.XPATH, self.country).send_keys(self.Country)

        self.driver.find_element(By.XPATH, self.city).send_keys(self.City)

        self.driver.find_element(By.XPATH, self.card).send_keys(self.special_character)

        self.driver.find_element(By.XPATH, self.month).send_keys(self.Null)

        self.driver.find_element(By.XPATH, self.year).send_keys(self.Null)

        self.driver.find_element(By.XPATH, self.close).click()


    @allure.step
    @allure.description("cart invalid placeholder address")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cart_page_secial_X(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.button).click()

        self.driver.find_element(By.XPATH, self.order).click()

        self.driver.find_element(By.XPATH, self.Xpath_name).send_keys(self.Name)

        self.driver.find_element(By.XPATH, self.country).send_keys(self.Country)

        self.driver.find_element(By.XPATH, self.city).send_keys(self.City)

        self.driver.find_element(By.XPATH, self.card).send_keys(self.special_character)

        self.driver.find_element(By.XPATH, self.month).send_keys(self.Null)

        self.driver.find_element(By.XPATH, self.year).send_keys(self.Null)

        self.driver.find_element(By.XPATH, self.X).click()


