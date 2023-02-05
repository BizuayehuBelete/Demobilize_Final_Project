import time
import allure
from allure_commons.types import AttachmentType

from selenium.webdriver.common.by import By

from dmobilaize.Base_test.test_base import Base_test
from dmobilaize.Locators.home_page_locator import *


class Home_page(Base_test):

    def __init__(self):

        self.iphone=Home_Page_Locators.iphone_6
        self.Add_Cart=Home_Page_Locators.Add_to_cart
        self.iphone_Assert=Home_Page_Locators.ipone_name
        self.cart = Home_Page_Locators.cart
        self.samsung=Home_Page_Locators.samsung_s6
        self.sums_assert=Home_Page_Locators.sumsung_name
        self.Next=Home_Page_Locators.next_button
        self.Sony=Home_Page_Locators.sony_vaio_5
        self.sony_name=Home_Page_Locators.Sony_name
        self.laptop=Home_Page_Locators.laptop_button
        self.monitor=Home_Page_Locators.monitor_button
        self.Apple_Monitor=Home_Page_Locators.Apple_monitor
        self.Apple_Name=Home_Page_Locators.Apple_name
        self.Nokia_lu=Home_Page_Locators.nokia_lumi
        self.Nokia_Name=Home_Page_Locators.Nokia_lumi_delete
        self.plceholder=Home_Page_Locators.place_order
        self.place_name=Home_Page_Locators.Place_holder_name
        self.name=Home_Page_Locators.pleaceholder_name
        self.cuntry=Home_Page_Locators.place_holder_cuntry
        self.cuntry_name=Home_Page_Locators.country
        self.city=Home_Page_Locators.place_holder_city
        self.pace_holder_city=Home_Page_Locators.city
        self.credit=Home_Page_Locators.creadit_card
        self.creadit_no_=Home_Page_Locators.card
        self.month_no=Home_Page_Locators.Month_card
        self.Month=Home_Page_Locators.month
        self.Year=Home_Page_Locators.year_please_holder
        self.year=Home_Page_Locators.year
        self.purchase=Home_Page_Locators.purchase
        self.logo=Home_Page_Locators.Logo
        self.MK_Book=Home_Page_Locators.makbook_air
        self.MK_name=Home_Page_Locators.mk_name
        self.sony_vov=Home_Page_Locators.sony_vaio_5
        self.sony_name=Home_Page_Locators.sony_vaio_name
        self.sony_7=Home_Page_Locators.sony_vaio_7
        self.sony_7_name=Home_Page_Locators.sony_vaio_7_name
        self.Dell_i7=Home_Page_Locators.dell_i7
        self.Dell_i7_name=Home_Page_Locators.dell_i7_name
        self.dell_15=Home_Page_Locators.dell_15
        self.dell_15_name=Home_Page_Locators.dell_15_name
        self.Apple=Home_Page_Locators.Apple_monitor
        self.Apple_name=Home_Page_Locators.Apple_name
        self.sony_xperia=Home_Page_Locators.sony_xperia
        self.sony_xperia_name=Home_Page_Locators.sony_xperia_name





    def common(self):
        super().base_for_web()

    @allure.step
    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self):
        self.common()
        logo=self.driver.find_element(By.XPATH,self.logo).is_displayed()
        if logo == True:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="testlogoscreen",
                          attachment_type=AttachmentType.PNG)
            assert False

    @allure.description("test iphone_6")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_iphone_6(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH,self.iphone).click()
        self.driver.find_element(By.XPATH,self.Add_Cart).click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()

        self.driver.find_element(By.XPATH, self.cart).click()
        title = self.driver.find_element(By.XPATH,self.iphone_Assert).text
        assert title == "Iphone 6 32gb"

        self.driver.find_element(By.XPATH,self.plceholder).click()

        self.Name_field = self.driver.find_element(By.XPATH, self.place_name)
        self.Name_field.clear()
        self.Name_field.send_keys(self.name)

        self.cuntry_field = self.driver.find_element(By.XPATH, self.cuntry)
        self.cuntry_field.clear()
        self.cuntry_field.send_keys(self.cuntry_name)
        self.city_field = self.driver.find_element(By.XPATH, self.city)
        self.city_field.clear()
        self.city_field.send_keys(self.pace_holder_city)
        self.credit_field = self.driver.find_element(By.XPATH, self.credit)
        self.credit_field.clear()
        self.credit_field.send_keys(self.creadit_no_)

        self.month_field = self.driver.find_element(By.XPATH, self.month_no)
        self.month_field.clear()
        self.month_field.send_keys(self.Month)

        self.year_field = self.driver.find_element(By.XPATH, self.Year)
        self.year_field.clear()
        self.year_field.send_keys(self.year)

        self.driver.find_element(By.XPATH,self.purchase).click()


    @allure.step
    @allure.description("test samsung_s6")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_samsung_s6(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.samsung).click()

        self.driver.find_element(By.XPATH, self.Add_Cart).click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()

        self.driver.find_element(By.XPATH, self.cart).click()

        title2 = self.driver.find_element(By.XPATH, self.sums_assert).text
        assert title2 == "Samsung galaxy s6"

        self.driver.find_element(By.XPATH, self.plceholder).click()

        self.Name_field = self.driver.find_element(By.XPATH, self.place_name)
        self.Name_field.clear()
        self.Name_field.send_keys(self.name)

        self.cuntry_field = self.driver.find_element(By.XPATH, self.cuntry)
        self.cuntry_field.clear()
        self.cuntry_field.send_keys(self.cuntry_name)
        self.city_field = self.driver.find_element(By.XPATH, self.city)
        self.city_field.clear()
        self.city_field.send_keys(self.pace_holder_city)
        self.credit_field = self.driver.find_element(By.XPATH, self.credit)
        self.credit_field.clear()
        self.credit_field.send_keys(self.creadit_no_)

        self.month_field = self.driver.find_element(By.XPATH, self.month_no)
        self.month_field.clear()
        self.month_field.send_keys(self.Month)

        self.year_field = self.driver.find_element(By.XPATH, self.Year)
        self.year_field.clear()
        self.year_field.send_keys(self.year)

        self.driver.find_element(By.XPATH, self.purchase).click()


    @allure.step
    @allure.description("test Assus_phone")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_assus(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")

        self.driver.find_element(By.XPATH, self.Sony).click()

        self.driver.find_element(By.XPATH, self.Add_Cart).click()
        time.sleep(3)
        self.driver.switch_to.alert.accept()

        self.driver.find_element(By.XPATH, self.cart).click()

        title3 = self.driver.find_element(By.XPATH, self.sony_name).text
        assert title3 == "Sony vaio i5"

        self.driver.find_element(By.XPATH, self.plceholder).click()

        self.holder_name = self.driver.find_element(By.XPATH, self.place_name)
        self.holder_name.clear()
        self.holder_name.send_keys(self.name)

        self.country_name = self.driver.find_element(By.XPATH, self.cuntry)
        self.country_name.clear()
        self.country_name.send_keys(self.cuntry_name)
        self.city_name = self.driver.find_element(By.XPATH, self.city)
        self.city_name.clear()
        self.city_name.send_keys(self.pace_holder_city)
        self.credit_name = self.driver.find_element(By.XPATH, self.credit)
        self.credit_name.clear()
        self.credit_name.send_keys(self.creadit_no_)

        self.month_filled = self.driver.find_element(By.XPATH, self.month_no)
        self.month_filled.clear()
        self.month_filled.send_keys(self.Month)

        self.year_filled = self.driver.find_element(By.XPATH, self.Year)
        self.year_filled.clear()
        self.year_filled.send_keys(self.year)
        self.driver.find_element(By.XPATH, self.purchase).click()


    @allure.step
    @allure.description("test Apple_monitor")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_apple_monitor(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.monitor).click()

        self.driver.find_element(By.XPATH, self.Apple_Monitor).click()

        self.driver.find_element(By.XPATH, self.Add_Cart).click()
        time.sleep(3)
        self.driver.switch_to.alert.accept()

        self.driver.find_element(By.XPATH, self.cart).click()

        title3 = self.driver.find_element(By.XPATH, self.Apple_Name).text
        assert title3 == "Apple monitor 24"

        self.driver.find_element(By.XPATH, self.plceholder).click()

        self.holder_name = self.driver.find_element(By.XPATH, self.place_name)
        self.holder_name.clear()
        self.holder_name.send_keys(self.name)

        self.country_name = self.driver.find_element(By.XPATH, self.cuntry)
        self.country_name.clear()
        self.country_name.send_keys(self.cuntry_name)
        self.city_name = self.driver.find_element(By.XPATH, self.city)
        self.city_name.clear()
        self.city_name.send_keys(self.pace_holder_city)
        self.credit_name = self.driver.find_element(By.XPATH, self.credit)
        self.credit_name.clear()
        self.credit_name.send_keys(self.creadit_no_)

        self.month_filled = self.driver.find_element(By.XPATH, self.month_no)
        self.month_filled.clear()
        self.month_filled.send_keys(self.Month)

        self.year_filled = self.driver.find_element(By.XPATH, self.Year)
        self.year_filled.clear()
        self.year_filled.send_keys(self.year)
        self.driver.find_element(By.XPATH, self.purchase).click()


    @allure.step
    @allure.description("test Nokia_lumi")
    @allure.severity(allure.severity_level.CRITICAL)
    def Test_Nokia_Lumui(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.Nokia_lu).click()
        self.driver.find_element(By.XPATH, self.Add_Cart).click()
        time.sleep(3)
        self.driver.switch_to.alert.accept()

        self.driver.find_element(By.XPATH, self.cart).click()

        self.driver.find_element(By.XPATH, self.Nokia_Name).click()

        self.driver.find_element(By.XPATH, self.plceholder).click()

        self.holder_name = self.driver.find_element(By.XPATH, self.place_name)
        self.holder_name.clear()
        self.holder_name.send_keys(self.name)

        self.country_name = self.driver.find_element(By.XPATH, self.cuntry)
        self.country_name.clear()
        self.country_name.send_keys(self.cuntry_name)
        self.city_name = self.driver.find_element(By.XPATH, self.city)
        self.city_name.clear()
        self.city_name.send_keys(self.pace_holder_city)
        self.credit_name = self.driver.find_element(By.XPATH, self.credit)
        self.credit_name.clear()
        self.credit_name.send_keys(self.creadit_no_)

        self.month_filled = self.driver.find_element(By.XPATH, self.month_no)
        self.month_filled.clear()
        self.month_filled.send_keys(self.Month)

        self.year_filled = self.driver.find_element(By.XPATH, self.Year)
        self.year_filled.clear()
        self.year_filled.send_keys(self.year)
        self.driver.find_element(By.XPATH, self.purchase).click()


    @allure.step
    @allure.description("test Mac_book_")
    @allure.severity(allure.severity_level.CRITICAL)
    def MK_book(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.laptop).click()
        self.driver.find_element(By.XPATH,self.MK_Book ).click()

        self.driver.find_element(By.XPATH, self.Add_Cart).click()
        time.sleep(3)
        self.driver.switch_to.alert.accept()

        self.driver.find_element(By.XPATH, self.cart).click()

        title3 = self.driver.find_element(By.XPATH, self.MK_name).text
        assert title3 =="MacBook air"

        self.driver.find_element(By.XPATH, self.plceholder).click()

        self.holder_name = self.driver.find_element(By.XPATH, self.place_name)
        self.holder_name.clear()
        self.holder_name.send_keys(self.name)

        self.country_name = self.driver.find_element(By.XPATH, self.cuntry)
        self.country_name.clear()
        self.country_name.send_keys(self.cuntry_name)
        self.city_name = self.driver.find_element(By.XPATH, self.city)
        self.city_name.clear()
        self.city_name.send_keys(self.pace_holder_city)
        self.credit_name = self.driver.find_element(By.XPATH, self.credit)
        self.credit_name.clear()
        self.credit_name.send_keys(self.creadit_no_)
        self.driver.find_element(By.XPATH, self.purchase).click()
        time.sleep(3)

        self.month_filled = self.driver.find_element(By.XPATH, self.month_no)
        self.month_filled.clear()
        self.month_filled.send_keys(self.Month)

        self.year_filled = self.driver.find_element(By.XPATH, self.Year)
        self.year_filled.clear()
        self.year_filled.send_keys(self.year)

    @allure.step
    @allure.description("test sony_v5")
    @allure.severity(allure.severity_level.CRITICAL)
    def sony_v5(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.laptop).click()
        self.driver.find_element(By.XPATH, self.sony_vov).click()

        self.driver.find_element(By.XPATH, self.Add_Cart).click()
        time.sleep(3)
        self.driver.switch_to.alert.accept()

        self.driver.find_element(By.XPATH, self.cart).click()

        title3 = self.driver.find_element(By.XPATH, self.sony_name).text
        assert title3 == "Sony vaio i5"

        self.driver.find_element(By.XPATH, self.plceholder).click()

        self.holder_name = self.driver.find_element(By.XPATH, self.place_name)
        self.holder_name.clear()
        self.holder_name.send_keys(self.name)

        self.country_name = self.driver.find_element(By.XPATH, self.cuntry)
        self.country_name.clear()
        self.country_name.send_keys(self.cuntry_name)
        self.city_name = self.driver.find_element(By.XPATH, self.city)
        self.city_name.clear()
        self.city_name.send_keys(self.pace_holder_city)
        self.credit_name = self.driver.find_element(By.XPATH, self.credit)
        self.credit_name.clear()
        self.credit_name.send_keys(self.creadit_no_)

        self.month_filled = self.driver.find_element(By.XPATH, self.month_no)
        self.month_filled.clear()
        self.month_filled.send_keys(self.Month)

        self.year_filled = self.driver.find_element(By.XPATH, self.Year)
        self.year_filled.clear()
        self.year_filled.send_keys(self.year)
        self.driver.find_element(By.XPATH, self.purchase).click()


    @allure.step
    @allure.description("test sony_v7")
    @allure.severity(allure.severity_level.CRITICAL)
    def sony_v7(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.laptop).click()
        self.driver.find_element(By.XPATH, self.sony_7).click()

        self.driver.find_element(By.XPATH, self.Add_Cart).click()
        time.sleep(3)
        self.driver.switch_to.alert.accept()

        self.driver.find_element(By.XPATH, self.cart).click()

        title3 = self.driver.find_element(By.XPATH, self.sony_7_name).text
        assert title3 == "Sony vaio i7"

        self.driver.find_element(By.XPATH, self.plceholder).click()

        self.holder_name = self.driver.find_element(By.XPATH, self.place_name)
        self.holder_name.clear()
        self.holder_name.send_keys(self.name)

        self.country_name = self.driver.find_element(By.XPATH, self.cuntry)
        self.country_name.clear()
        self.country_name.send_keys(self.cuntry_name)
        self.city_name = self.driver.find_element(By.XPATH, self.city)
        self.city_name.clear()
        self.city_name.send_keys(self.pace_holder_city)
        self.credit_name = self.driver.find_element(By.XPATH, self.credit)
        self.credit_name.clear()
        self.credit_name.send_keys(self.creadit_no_)

        self.month_filled = self.driver.find_element(By.XPATH, self.month_no)
        self.month_filled.clear()
        self.month_filled.send_keys(self.Month)

        self.year_filled = self.driver.find_element(By.XPATH, self.Year)
        self.year_filled.clear()
        self.year_filled.send_keys(self.year)
        self.driver.find_element(By.XPATH, self.purchase).click()


    @allure.step
    @allure.description("test dell_i7")
    @allure.severity(allure.severity_level.CRITICAL)
    def dell_i7(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.laptop).click()
        self.driver.find_element(By.XPATH, self.Dell_i7).click()

        self.driver.find_element(By.XPATH, self.Add_Cart).click()
        time.sleep(3)
        self.driver.switch_to.alert.accept()

        self.driver.find_element(By.XPATH, self.cart).click()

        title3 = self.driver.find_element(By.XPATH, self.Dell_i7_name).text
        assert title3 == "Dell i7 8gb"

        self.driver.find_element(By.XPATH, self.plceholder).click()

        self.holder_name = self.driver.find_element(By.XPATH, self.place_name)
        self.holder_name.clear()
        self.holder_name.send_keys(self.name)

        self.country_name = self.driver.find_element(By.XPATH, self.cuntry)
        self.country_name.clear()
        self.country_name.send_keys(self.cuntry_name)
        self.city_name = self.driver.find_element(By.XPATH, self.city)
        self.city_name.clear()
        self.city_name.send_keys(self.pace_holder_city)
        self.credit_name = self.driver.find_element(By.XPATH, self.credit)
        self.credit_name.clear()
        self.credit_name.send_keys(self.creadit_no_)

        self.month_filled = self.driver.find_element(By.XPATH, self.month_no)
        self.month_filled.clear()
        self.month_filled.send_keys(self.Month)

        self.year_filled = self.driver.find_element(By.XPATH, self.Year)
        self.year_filled.clear()
        self.year_filled.send_keys(self.year)
        self.driver.find_element(By.XPATH, self.purchase).click()


    @allure.step
    @allure.description("test Dell_15.6")
    @allure.severity(allure.severity_level.CRITICAL)
    def dell_15_15(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.laptop).click()
        self.driver.find_element(By.XPATH, self.dell_15).click()

        self.driver.find_element(By.XPATH, self.Add_Cart).click()
        time.sleep(3)
        self.driver.switch_to.alert.accept()

        self.driver.find_element(By.XPATH, self.cart).click()

        title3 = self.driver.find_element(By.XPATH, self.dell_15_name).text
        assert title3 == "2017 Dell 15.6 Inch"

        self.driver.find_element(By.XPATH, self.plceholder).click()

        self.holder_name = self.driver.find_element(By.XPATH, self.place_name)
        self.holder_name.clear()
        self.holder_name.send_keys(self.name)

        self.country_name = self.driver.find_element(By.XPATH, self.cuntry)
        self.country_name.clear()
        self.country_name.send_keys(self.cuntry_name)
        self.city_name = self.driver.find_element(By.XPATH, self.city)
        self.city_name.clear()
        self.city_name.send_keys(self.pace_holder_city)
        self.credit_name = self.driver.find_element(By.XPATH, self.credit)
        self.credit_name.clear()
        self.credit_name.send_keys(self.creadit_no_)

        self.month_filled = self.driver.find_element(By.XPATH, self.month_no)
        self.month_filled.clear()
        self.month_filled.send_keys(self.Month)

        self.year_filled = self.driver.find_element(By.XPATH, self.Year)
        self.year_filled.clear()
        self.year_filled.send_keys(self.year)
        self.driver.find_element(By.XPATH, self.purchase).click()


    @allure.step
    @allure.description("test Apple_Monitor")
    @allure.severity(allure.severity_level.CRITICAL)
    def Apple_monitor(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.monitor).click()
        self.driver.find_element(By.XPATH, self.Apple_Monitor).click()

        self.driver.find_element(By.XPATH, self.Add_Cart).click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()

        self.driver.find_element(By.XPATH, self.cart).click()

        title3 = self.driver.find_element(By.XPATH, self.Apple_Name).text
        assert title3 == "Apple monitor 24"

        self.driver.find_element(By.XPATH, self.plceholder).click()

        self.holder_name = self.driver.find_element(By.XPATH, self.place_name)
        self.holder_name.clear()
        self.holder_name.send_keys(self.name)

        self.country_name = self.driver.find_element(By.XPATH, self.cuntry)
        self.country_name.clear()
        self.country_name.send_keys(self.cuntry_name)
        self.city_name = self.driver.find_element(By.XPATH, self.city)
        self.city_name.clear()
        self.city_name.send_keys(self.pace_holder_city)
        self.credit_name = self.driver.find_element(By.XPATH, self.credit)

        self.credit_name.send_keys(self.creadit_no_)

        self.month_filled = self.driver.find_element(By.XPATH, self.month_no)
        self.month_filled.clear()
        self.month_filled.send_keys(self.Month)

        self.year_filled = self.driver.find_element(By.XPATH, self.Year)
        self.year_filled.clear()
        self.year_filled.send_keys(self.year)
        self.driver.find_element(By.XPATH, self.purchase).click()


    @allure.step
    @allure.description("test sony_xphria")
    @allure.severity(allure.severity_level.CRITICAL)
    def sony_xphria(self):
        self.common()
        self.driver.implicitly_wait(5)
        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, self.monitor).click()
        self.driver.find_element(By.XPATH, self.sony_xperia).click()

        self.driver.find_element(By.XPATH, self.Add_Cart).click()

        time.sleep(2)
        self.driver.switch_to.alert.accept()

        self.driver.find_element(By.XPATH, self.cart).click()

        title3 = self.driver.find_element(By.XPATH, self.sony_xperia_name).text
        assert title3 == "Sony xperia z5"

        self.driver.find_element(By.XPATH, self.plceholder).click()

        self.holder_name = self.driver.find_element(By.XPATH, self.place_name)
        self.holder_name.clear()
        self.holder_name.send_keys(self.name)

        self.country_name = self.driver.find_element(By.XPATH, self.cuntry)
        self.country_name.clear()
        self.country_name.send_keys(self.cuntry_name)
        self.city_name = self.driver.find_element(By.XPATH, self.city)
        self.city_name.clear()
        self.city_name.send_keys(self.pace_holder_city)
        self.credit_name = self.driver.find_element(By.XPATH, self.credit)
        self.credit_name.clear()
        self.credit_name.send_keys(self.creadit_no_)

        self.month_filled = self.driver.find_element(By.XPATH, self.month_no)
        self.month_filled.clear()
        self.month_filled.send_keys(self.Month)

        self.year_filled = self.driver.find_element(By.XPATH, self.Year)
        self.year_filled.clear()
        self.year_filled.send_keys(self.year)
        self.driver.find_element(By.XPATH, self.purchase).click()









