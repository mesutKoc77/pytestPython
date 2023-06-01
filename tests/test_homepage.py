from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
class TestHomepage:
    def test_top_menu_items(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://demowebshop.tricentis.com/")
        expected_menu = ["BOOKS", "COMPUTERS", "ELECTRONICS", "APPAREL & SHOES", "DIGITAL DOWNLOADS",
                         "JEWELRY", "GIFT CARDS"]
        elements = driver.find_elements(By.CSS_SELECTOR, "ul.top-menu>li>a")

        actual_menu_items=[]
        for i in elements:
            actual_menu_items.append(i.text)

        for i in range(len(expected_menu)):
            assert expected_menu[i]==actual_menu_items[i]
        driver.quit()

    def test_urun_ismine_tiklar_ve_urun_sayfasi_acilir(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://demowebshop.tricentis.com/")
        ilkurunlinki=driver.find_element(By.CSS_SELECTOR,"div.product-item h2 a")
        urun_ismi=ilkurunlinki.text
        urunfiyati=driver.find_element(By.CSS_SELECTOR,"span.price.actual-price").text
        ilkurunlinki.click()
        urunismidetaysayfasi=driver.find_element(By.CSS_SELECTOR,"div.product-name h1").text.strip()
        urunfiyatidetaysayfasi=driver.find_element(By.CSS_SELECTOR,"div.product-price span").text.strip()

        assert urun_ismi==urunismidetaysayfasi
        assert urunfiyati==urunfiyatidetaysayfasi

        driver.quit()













