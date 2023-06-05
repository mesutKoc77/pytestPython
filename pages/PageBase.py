from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PageBase:

    #sleenium webdriver bir class tan bir baska class a gecerken Driver veya browser otomatik o Class a gecmiyor
    #bizim o class a ilgili webdriver i tanimlamamiz gerekiyor.

    #page lerde kullanacgimiz tum ortak fonksiyonlari buraya koyacagiz. Mesela wait fonksiyonu gerekiyor
    #o zaman bir tane tanimlarim ve buraya koyarim.
    #meslea urun_detay_sayfasi page inde wait.sleep kullanacgm  ve bir cok foksiyonda bunu kullanacaksam
    #bu fonksiyonu PageBase e ekleyebilirim.

    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(self.driver, 30) #asagida bircok foksiyon da wait degiskenini kullandigim icin
        #surekli yeni bir wait tanimlamak yerine __init__ foknsiyon seviyesinde bir tane tanimladim ve
        #asagoidan surekli cagirdim.
        #bir bir deyisle instance variable olarak class seviyesine ekledim.

    def webelement_listesinden_string_listesi_ver(self, locator):
        elements = self.driver.find_elements(*locator)
        liste = []
        for i in elements:
            liste.append(i.text)
        return liste



    def wait_element_visibility(self, locator):

        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return element

    def wait_element_presence(self, locator):

        element = self.wait.until(expected_conditions.presence_of_element_located(locator))
        return element

    def wait_alert_presence(self):
        self.wait.until(expected_conditions.alert_is_present())








