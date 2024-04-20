from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    NEWS = "//*[@id='s-top-left']/a[1]"
    HAO123 = "//*[@id='s-top-left']/a[2]"
    MAP = "//*[@id='s-top-left']/a[3]"
    DISCUSSION = "//*[@id='s-top-left']/a[4]"
    VIDEO = "//*[@id='s-top-left']/a[5]"
    IMAGE = "//*[@id='s-top-left']/a[6]"
    BODY = "name"

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open_url(self, url):
        self.driver.get(url)

    @property
    def get_title(self):
        return self.driver.title

    @property
    def get_url(self):
        return self.driver.current_url

    @property
    def target_attribute(self):
        return self.driver.find_element(By.XPATH, self.NEWS).get_attribute("target")

    @property
    def href_attribute(self):
        return self.driver.find_element(By.XPATH, self.NEWS).get_attribute("href")

    @property
    def get_news(self):
        return self.driver.find_element(By.XPATH, self.NEWS)

    def click_news(self):
        # self.driver.execute_script("arguments[0].removeAttribute('target');", self.get_news)
        self.get_news.click()
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        all_handles = self.driver.window_handles
        print(f"============={all_handles}")
        return self.driver.switch_to.window(all_handles[1])


    @property
    def get_hao123(self):
        return self.driver.find_element(By.XPATH, self.HAO123)

    def click_hao123(self):
        return self.get_hao123.click()

    @property
    def get_map(self):
        return self.driver.find_element(By.XPATH, self.MAP)

    def click_map(self):
        return self.get_map.click()

    @property
    def get_discussion(self):
        return self.driver.find_element(By.XPATH, self.DISCUSSION)

    def click_discussion(self):
        return self.get_discussion.click()

    @property
    def get_video(self):
        return self.driver.find_element(By.XPATH, self.VIDEO)

    def click_video(self):
        return self.get_video.click()

    @property
    def get_image(self):
        return self.driver.find_element(By.XPATH, self.IMAGE)

    def click_image(self):
        return self.get_image.click()



