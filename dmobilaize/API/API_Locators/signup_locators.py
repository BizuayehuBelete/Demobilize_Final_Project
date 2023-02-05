from random import randint

class RegisterConstants:
    num = randint(1, 2500)
    url_register = 'https://api.demoblaze.com/signup'
    data_valid = {'name': "Bizuayehu",
                  'password': "bizu"}
    data_invalid_passwerd = {'name': "Belete",
                             'password': "ewgefuwtyg"}
    data_invalid_Null_user_name = {'name': " ",
                                    'password': "bizu"}
    data_invalid_Null_passwerd = {'name': "Bizeuwgdbdd ",
                                   'password': ""}
    data_invalid_invalid_user_name = {'name': "hdgfffhdh",
                                    'password':"dfbhdbfh"}