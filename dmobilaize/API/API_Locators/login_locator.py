from random import randint


class LoginConstants:
    num = randint(1, 2500)
    url_login = 'https://api.demoblaze.com/login'
    success_key = 'success'
    message_key = 'message'
    data_valid = {"email": "bBizuayehu", "password": f"Bizu@{123}"}
    data_invalid_password = {"email": "sgdhd", "password": "dshd"}
    data_invalid_email = {"email": "dfhds", "password": "dhbdssdf"}
    data_invalid_password_and_email = {"email": "djkhfsd", "password": "fhdsdhg"}
    data_null_password_and_email = {"email": " " "password" " "}