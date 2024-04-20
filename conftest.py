import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

load_dotenv()


def pytest_addoption(parser):
    parser.addoption(
        "--driver",
        action="store",
        default="chrome",
        help="Choose your driver",
    )


@pytest.fixture(autouse=True, scope="function")
def init_driver(request):
    driver = ''
    driver_service = request.config.getoption('--driver')
    # driver_service = os.getenv("DRIVER")
    print(f'----------{driver_service}')
    match driver_service:
        case "chrome":
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())
        case "safari":
            driver = webdriver.Safari(options=webdriver.SafariOptions())
        case "firefox":
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=webdriver.FirefoxOptions())
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    out = yield
    report = out.get_result()

    # print(call)
    # we can mark testcase failed in testrail through api
    if report.when == "call":
        print(report)
        print("---------------------------")
        print(item.name)
        print(report.outcome)
