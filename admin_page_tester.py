from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class AdminPageTester:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
        time.sleep(2)

    def create_user(self, user_info):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/button').click()

        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys(user_info["firstName"])
        self.driver.find_element(By.XPATH, '//*[@id="lastName"]').send_keys(user_info["lastName"])
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(user_info["username"])
        self.driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(user_info["phoneNumber"])
        self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(user_info["email"])

        # generate password
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/form/div[1]/div[6]/button').click()

        # select role
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/form/div[1]/div[7]/div/div').click()
        if user_info["role"] == "manager":
            self.driver.find_element(By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[1]').click()
        else:
            self.driver.find_element(By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[2]').click()

        # select sex
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/form/div[1]/div[8]/div/div').click()
        if user_info["sex"] == "Male":
            self.driver.find_element(By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[1]').click()
        else:
            self.driver.find_element(By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[2]').click()

        # submit form
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/form/div[2]/button[2]').click()
        time.sleep(5)

    def search_user(self, query):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div/div/div/input').send_keys(query)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div/div/div/input').send_keys(
            Keys.ENTER)
        time.sleep(2)

    def go_to_active_tab(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div/div/button[2]').click()
        time.sleep(2)

    def go_to_inactive_tab(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div/div/button[3]').click()
        time.sleep(2)

    def go_to_home_page(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/button').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="menu-appbar"]/div[3]/ul/ul/li[1]').click()
        time.sleep(2)

    def logout(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/button').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="menu-appbar"]/div[3]/ul/ul/li[2]').click()
        time.sleep(2)

    def run_test(self):
        self.login("admin", "password")

        manager_info = {
            "firstName": "Kelvin",
            "lastName": "Lai",
            "sex": "Male",
            "email": "kelvin_lai@fujitsu.com",
            "phoneNumber": "88888888",
            "role": "manager",
            "username": "kelvin"
        }
        self.create_user(manager_info)

        worker_info = {
            "firstName": "Harry",
            "lastName": "Yau",
            "sex": "Male",
            "email": "harry_yau@fujitsu.com1241243421",
            "phoneNumber": "12345678",
            "role": "worker",
            "username": "harry"
        }
        self.create_user(worker_info)

        self.search_user("kelvin")
        self.go_to_active_tab()
        self.go_to_inactive_tab()

        self.go_to_home_page()
        self.logout()


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service(executable_path=ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=service, options=options)
    chrome_driver.get("http://localhost:3000")

    admin_page_tester = AdminPageTester(chrome_driver)
    admin_page_tester.run_test()
