import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.safari.service import Service



@pytest.fixture(scope="class")
def setup(request, browser):
    if browser=="chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser=="firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "safari":  # bu projede safari kullanilmadi, ornek icin konuldu
        # safarinin kullanimina iliskin hocanin python selenium video serisi var orada chrome driver i nasil ekledi
        # ise oraya safari driver da eklenebilir.
        service = Service("./drivers/safari")
        driver = webdriver.Chrome(service=service)
    else:
        print("heeey dogru durust bir tarayici gir")
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")
