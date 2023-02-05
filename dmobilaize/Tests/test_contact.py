import allure
import pytest
from pytest import mark
from dmobilaize.Page_test.contact_page import Contact_Page


class Test_Contact():
    @allure.description("test_contact_message")
    @pytest.mark.sanity
    def test_contact_message(self):
        test = Contact_Page()
        test.contact()

    @allure.description("test_invalid_address")
    @pytest.mark.sanity
    def test_invalid_address(self):
        test = Contact_Page()
        test.steps_invalid_email()

    @allure.description("test_close_button")
    @pytest.mark.sanity
    def test_close_button(self):
        test = Contact_Page()
        test.close_button()

    @allure.description("test_X_button")
    @pytest.mark.sanity
    def test_X_button(self):
        test = Contact_Page()
        test.X_button()

    @allure.description("test_contact_NULL")
    @pytest.mark.sanity
    def test_contact_NULL(self):
        test = Contact_Page()
        test.Test_contact_NULL()

