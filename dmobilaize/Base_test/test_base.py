from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base_test():

    def base_for_web(self):

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10) # seconds
        self.driver.get("https://www.demoblaze.com/index.html")
        driver = webdriver.Chrome(executable_path=r'D:PATHchromedriver.exe')

        self.driver.maximize_window()
        return self.driver

    def close(self):
        self.driver.quit()
        self.driver.close()
