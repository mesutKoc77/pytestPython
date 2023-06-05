
from selenium.webdriver.common.by import By

from pages.PageBase import PageBase


class Anasayfa(PageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver
        # sleenium webdriver bir class tan bir baska class a gecerken Driver veya browser otomatik o Class a gecmiyor
        # bizim o class a ilgili webdriver i tanimlamamiz gerekiyor.
        #driver im yani browser im parametre olark fonksiyon da verdgim driver a esit olacak. Diger bir deyisle
        #ilgili class da aldigi driver i getirecek buraya atayacak.

    UST_MENU_LINKLERI=(By.CSS_SELECTOR, "ul.top-menu>li>a")
    ILK_URUN_ISMI=(By.CSS_SELECTOR,"div.product-item h2 a")
    ILK_GIFT_CARD_OLMAYAN_URUN_ISMI=(By.XPATH, "//div[@class='item-box']//h2/a[not(contains(text(),'Gift Card'))]")
    ILK_URUN_FIYATI=(By.CSS_SELECTOR,"span.price.actual-price")



    def ust_menu_isimlerini_liste_ver(self):
       return self.webelement_listesinden_string_listesi_ver(Anasayfa.UST_MENU_LINKLERI)

    def ilk_urun_ismini_ver(self):
        ilkurunlinki=self.driver.find_element(*Anasayfa.ILK_URUN_ISMI)
        return ilkurunlinki.text

    def ilk_urun_fiyatini_ver(self):
        return self.driver.find_element(*Anasayfa.ILK_URUN_FIYATI).text

    def ilk_urun_ismine_tikla(self):
        ilk_urun_ismi= self.wait_element_visibility(Anasayfa.ILK_URUN_ISMI)
        ilk_urun_ismi.click()
    def gift_card_olmayan_ilk_urun_ismine_tikla(self):
        self.driver.find_element(*Anasayfa.ILK_GIFT_CARD_OLMAYAN_URUN_ISMI).click()


