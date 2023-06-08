import unittest

import pytest
from ddt import ddt, data, unpack

from pages.arama_sayfasi import AramaSayfasi
from utilities.ExcelYardimcisi import ExcelYardimcisi


@pytest.mark.usefixtures("setup")

@ddt #data driven test
class TestArama(unittest.TestCase):

    # Bu örnekteki gibi veriyi elle yazmak iyi uygulama değil.
    # Bunun yerine aşağıdaki gibi excelden veriyi almak daha doğru
    #@data(("ab", "Search term minimum length is 3 characters"),
          #("abc", "No products were found that matched your criteria."))
  # @unpack
   # def test_arama_uyari_verir(self, kelime, beklenen_mesaj):
        #self.driver.get("https://demowebshop.tricentis.com/")
        #arama = AramaSayfasi(self.driver)
        #arama.arama_yap(kelime)
       # mesaj = arama.arama_uyari_mesajini_ver()
        #assert mesaj == beklenen_mesaj


    @data(*ExcelYardimcisi.excel_listeler_listesine_cevir("./testdata/arama.xlsx","Sheet1") )
    @unpack
    def test_arama(self, senaryoturu, kelime, beklenen_mesaj):
        self.driver.get("https://demowebshop.tricentis.com/")
        # simdi arama_sayfasi ndaki methodlara ulasabilmek icin AramaSayfasi class indan bir obje olusturacag#
        arama=AramaSayfasi(self.driver)
        arama.arama_yap(kelime)
        if senaryoturu.lower()=="negatif":
            mesaj = arama.arama_uyari_mesajini_ver()
            assert mesaj == beklenen_mesaj
            # burada ddt yi yukledik terminalden
        elif senaryoturu.lower()=="pozitif":
            urun_isimleri=arama.aranan_urun_isimlerini_liste_ver()
            for isim in urun_isimleri:
                assert kelime.lower() in isim.lower()

















