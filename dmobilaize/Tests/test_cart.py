import pytest
from pytest import mark

from dmobilaize.Page_test.cart_page import *


class Test_cart:
    @allure.description("test_aboutus_X")
    @pytest.mark.sanity
    def test_cart(self):
        test = Cart_page()
        test.test_cart_page()

    @allure.description("test_cart_page_invalid")
    @pytest.mark.sanity
    def test_cart_page_invalid(self):
        test = Cart_page()
        test.test_cart_page_invalid()

    @allure.description("test_cart_page_secial_character")
    @pytest.mark.sanity
    def test_cart_page_secial_character(self):
        test = Cart_page()
        test.test_cart_page_secial_character()

    @allure.description("test_cart_page_secial_characterand_Null")
    @pytest.mark.sanity
    def test_cart_page_secial_characterand_Null(self):
        test=Cart_page()
        test.test_cart_page_secial_characterand_Null()

    @allure.description("test_cart_page_secial_close")
    @pytest.mark.sanity
    def test_cart_page_secial_close(self):
        test = Cart_page()
        test.test_cart_page_secial_close()

    @allure.description("test_cart_page_secial_X")
    @pytest.mark.sanity
    def test_cart_page_secial_X(self):
        test = Cart_page()
        test.test_cart_page_secial_X()





