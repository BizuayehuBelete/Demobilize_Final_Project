import pytest
from pytest import mark
from dmobilaize.Page_test.Aboutus_Page import *


class Test_About_us:
    @allure.description("test_aboutus_page")
    @pytest.mark.sanity
    def test_aboutus_page(self):
        test = Aboutus_page()
        test.test_aboutus_page()

    @allure.description("test_aboutus_close")
    @pytest.mark.sanity
    def test_aboutus_close(self):
        test = Aboutus_page()
        test.test_aboutus_page()

    @allure.description("test_aboutus_X")
    @pytest.mark.sanity
    def test_aboutus_X(self):
        test = Aboutus_page()
        test.test_aboutus_page()
