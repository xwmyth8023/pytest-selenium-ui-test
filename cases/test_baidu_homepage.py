import allure
from pages.base_page import BasePage

@allure.title("检查并点击news链接")
def test_news_link(init_driver):
    with allure.step("初始化driver"):
        homepage = BasePage(init_driver)
    with allure.step("打开百度首页"):
        homepage.open_url("http://www.baidu.com")
    assert "百度一下，你就知道" == homepage.get_title
    assert homepage.target_attribute == "_blank"
    assert homepage.href_attribute == "http://news.baidu.com/"
    with allure.step("点击news链接"):
        homepage.click_news()
    assert homepage.get_url == "https://news.baidu.com/"

def test_hao123_link(init_driver):
    homepage = BasePage(init_driver)
    homepage.open_url("http://www.baidu.com")
    homepage.click_hao123()

def test_discussion_link(init_driver):
    homepage = BasePage(init_driver)
    homepage.open_url("http://www.baidu.com")
    homepage.click_discussion()


def test_map_link(init_driver):
    homepage = BasePage(init_driver)
    homepage.open_url("http://www.baidu.com")
    homepage.click_map()

def test_video_link(init_driver):
    homepage = BasePage(init_driver)
    homepage.open_url("http://www.baidu.com")
    homepage.click_video()

def test_image_link(init_driver):
    homepage = BasePage(init_driver)
    homepage.open_url("http://www.baidu.com")
    homepage.click_image()
