import allure

@allure.title('Test Case 1: 验证1等于1')
def test_cases1(init_driver):
    init_driver.get("https://www.baidu.com")
    assert 1 == 1

@allure.title('Test Case 2: 验证1不等于2')
def test_cases2():
    assert 1 == 2
