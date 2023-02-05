# import allure
import allure
import pytest

from dmobilaize.Page_test.login_page import *
from pytest import mark

class Test_Signin_Test:
    @allure.description("test_Login_close_button")
    @pytest.mark.sanity
    def test_Login_close_button(self):
        test = Login_Page()
        test.close_button()

    @allure.description("test_login")
    @pytest.mark.sanity
    def test_login(self):
        test = Login_Page()
        test.signin()

    @allure.description("test_Login")
    @pytest.mark.sanity
    def test_Login(self):
        test = Login_Page()
        test.invalid_signin()

    @allure.description("test_Login_special_character")
    @pytest.mark.sanity
    def test_Login_special_character(self):
        test = Login_Page()
        test.special_character_signin()

    @allure.description("test_Login_specialand_null")
    @pytest.mark.sanity
    def test_Login_specialand_null(self):
        test = Login_Page()
        test.special_and_Null()

    @allure.description("test_Login_Null")
    @pytest.mark.sanity
    def test_Login_Null(self):
        test = Login_Page()
        test.special_Null_password()
