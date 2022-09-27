from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class WorkerPageTester:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="kc-login"]').click()
        time.sleep(2)

    def create_job(self, job_info):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/button').click()

        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="code"]').send_keys(job_info["code"])
        self.driver.find_element(By.XPATH, '//*[@id="title"]').send_keys(job_info["title"])
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[3]/div/div/div/input').click()
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[3]/div/div/div/input').send_keys(
            Keys.ARROW_DOWN)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[3]/div/div/div/input').send_keys(
            Keys.ENTER)
        self.driver.find_element(By.XPATH, '//*[@id="description"]').send_keys(job_info["description"])

        # submit form
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/form/div[2]/button[2]').click()
        time.sleep(2)

    def search_job(self, query):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div/div/div/input').send_keys(query)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div/div/div/input').send_keys(
            Keys.ENTER)
        time.sleep(2)

    def complete_job(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="root"]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[6]/button').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[2]/button[2]').click()
        time.sleep(2)

    def go_to_in_progress_tab(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div/div/button[2]').click()
        time.sleep(2)

    def go_to_completed_tab(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div/div/button[3]').click()
        time.sleep(2)

    def go_to_home_page(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/button').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="menu-appbar"]/div[3]/ul/ul/li[1]').click()
        time.sleep(2)

    def go_to_profile(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/button').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="menu-appbar"]/div[3]/ul/ul/li[2]').click()
        time.sleep(2)

    def logout(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[2]/button').click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="menu-appbar"]/div[3]/ul/ul/li[3]').click()
        time.sleep(2)

    def run_test(self):
        self.login("harry", "password")

        self.search_job("5")

        self.complete_job()

        self.go_to_in_progress_tab()
        self.go_to_completed_tab()

        self.go_to_home_page()
        self.go_to_profile()
        self.logout()


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service(executable_path=ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=service, options=options)
    chrome_driver.get("http://localhost:3000")

    worker_page_tester = WorkerPageTester(chrome_driver)
    worker_page_tester.run_test()
