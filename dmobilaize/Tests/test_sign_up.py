import pytest
from pytest import mark
from dmobilaize.Page_test.sign_page import *


class Test_Sign_in:
    @allure.description("test_Signup")
    @pytest.mark.sanity
    def test_Signup(self):
        test = Signin_Page()
        test.sign_up_test()

    @allure.description("test_Signup_null")
    @pytest.mark.sanity
    def test_Signup_special_character(self):
        test = Signin_Page()
        test.sign_up_test_with_special_character()

    @allure.description("test_Signup_null")
    @pytest.mark.sanity
    def test_Signup_null(self):
        test = Signin_Page()
        test.sign_up_test_with_Null()

    @allure.description("test_Signup_close")
    @pytest.mark.sanity
    def test_Signup_close(self):
        test = Signin_Page()
        test.sign_up_test_close()

    @allure.description("test_invalid_password")
    @pytest.mark.sanity
    def test_invalid_password(self):
        test = Signin_Page()
        test.test_short_password()

    @allure.description("test_sign_up_X_button")
    @pytest.mark.sanity
    def test_sign_up_X_button(self):
        test = Signin_Page()
        test.test_sign_up_X_button()

    @allure.description("test_name_null")
    @pytest.mark.sanity
    def test_name_null(self):
        test = Signin_Page()
        test.test_name_null()

    @allure.description("test_password_null")
    @pytest.mark.sanity
    def test_password_null(self):
        test = Signin_Page()
        test.test_password_null()

    @allure.description("test_name_specilcharacter")
    @pytest.mark.sanity
    def test_name_specilcharacter(self):
        test = Signin_Page()
        test.test_name_specilcharacter()
