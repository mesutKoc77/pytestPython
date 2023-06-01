import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class TestHomepage:
    def test_top_menu_items(self):

        expected_menu = ["BOOKS", "COMPUTERS", "ELECTRONICS", "APPAREL & SHOES", "DIGITAL DOWNLOADS",
                         "JEWELRY", "GIFT CARDS"]
        elements = self.driver.find_elements(By.CSS_SELECTOR, "ul.top-menu>li>a")

        actual_menu_items=[]
        for i in elements:
            actual_menu_items.append(i.text)

        for i in range(len(expected_menu)):
            assert expected_menu[i]==actual_menu_items[i]


    def test_urun_ismine_tiklar_ve_urun_sayfasi_acilir(self):

        self.driver.get("https://demowebshop.tricentis.com/")
        ilkurunlinki=self.driver.find_element(By.CSS_SELECTOR,"div.product-item h2 a")
        urun_ismi=ilkurunlinki.text
        urunfiyati=self.driver.find_element(By.CSS_SELECTOR,"span.price.actual-price").text
        ilkurunlinki.click()
        urunismidetaysayfasi=self.driver.find_element(By.CSS_SELECTOR,"div.product-name h1").text.strip()
        urunfiyatidetaysayfasi=self.driver.find_element(By.CSS_SELECTOR,"div.product-price span").text.strip()

        assert urun_ismi==urunismidetaysayfasi
        assert urunfiyati==urunfiyatidetaysayfasi














