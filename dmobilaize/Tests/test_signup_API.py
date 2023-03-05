import allure
import requests
from dmobilaize.API.API_Locators.signup_locators import *

class Test_Register(RegisterConstants):
    @allure.description('User registered correctly')
    def test_user_register_correctly(self):
        url = RegisterConstants.url_register
        data = RegisterConstants.valid_data
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10


    @allure.description('User registered with exist email')
    def test_user_register_incorrectly_with_exist_email(self):
        url = RegisterConstants.url_register
        data = RegisterConstants.data_invalid_passwerd
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 10

    @allure.description('User registered with exist paswerd')
    def test_user_register_incorrectly_with_exist_passwerd(self):
        url = RegisterConstants.url_register
        data = RegisterConstants.data_invalid_Null_user_name
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 10
    #
    @allure.description('User registered with capital letter')
    def test_user_register_incorrectly_with_exist_email(self):
            url = RegisterConstants.url_register
            data = RegisterConstants.data_invalid_Null_passwerd
            res = requests.post(url, json=data)
            res_data = res.json()
            assert res.status_code == 400
            assert res.elapsed.total_seconds() < 10
    #
    @allure.description('User registered with exist email')
    def test_user_register_special_charactor_(self):
                url = RegisterConstants.url_register
                data = RegisterConstants.data_invalid_invalid_user_name
                res = requests.post(url, json=data)
                res_data = res.json()
                assert res.status_code == 400
                assert res.elapsed.total_seconds() < 10

    @allure.description('User registered with exist email')
    def test_user_register_incorrectly_with_null_body(self):
        url = RegisterConstants.url_register
        data = {}
        res = requests.post(url, json=data)
        assert res.status_code == 400