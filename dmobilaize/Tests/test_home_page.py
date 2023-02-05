import allure
import pytest

from dmobilaize.Page_test.home_page import *

from pytest import mark
class Test_Home:
    @allure.description("test_iphon_6")
    @pytest.mark.sanity
    def test_iphon_6(self):
        test = Home_page()
        test.test_iphone_6()

    @allure.description("test_sumsung_s")
    @pytest.mark.sanity
    def test_sumsung_s(self):
        test = Home_page()
        test.test_samsung_s6()

    @allure.description("test_assus_full_HD")
    @pytest.mark.sanity
    def test_assus_full_HD(self):
        test = Home_page()
        test.test_assus()

    @allure.description("test_Apple_Monitor")
    @pytest.mark.sanity
    def test_Apple_Monitor(self):
        test = Home_page()
        test.test_apple_monitor()

    @allure.description("test_Nokia_Lumi")
    @pytest.mark.sanity
    def test_Nokia_Lumi(self):
        test = Home_page()
        test.Test_Nokia_Lumui()

    @allure.description("test_logo")
    @pytest.mark.sanity
    def test_logo(self):
        test=Home_page()
        test.test_logo()

    @allure.description("test_MK_book")
    @pytest.mark.sanity
    def  test_MK_book(self):
        test = Home_page()
        test.MK_book()

    @allure.description("test_sony_v5")
    @pytest.mark.sanity
    def test_sony_v5(self):
        test = Home_page()
        test.sony_v5()

    @allure.description("test_sony_v7")
    @pytest.mark.sanity
    def test_sony_v7(self):
        test = Home_page()
        test.sony_v7()

    @allure.description("test_dell_i7")
    @pytest.mark.sanity
    def test_dell_i7(self):
        test = Home_page()
        test.dell_i7()

    @allure.description("test_dell_15_15")
    @pytest.mark.sanity
    def test_dell_15_15(self):
        test=Home_page()
        test.dell_15_15()

    @allure.description("test_Apple_monitor")
    @pytest.mark.sanity
    def test_Apple_monitor(self):
        test=Home_page()
        test.Apple_monitor()

    @allure.description("test_sony_xphria")
    @pytest.mark.sanity
    def test_sony_xphria(self):
        test = Home_page()
        test.sony_xphria()


