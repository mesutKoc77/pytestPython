import unittest

import pytest
from ddt import ddt, data, unpack

from pages.arama_sayfasi import AramaSayfasi


@pytest.mark.usefixtures("setup")

@ddt #data driven test
class TestArama(unittest.TestCase):

    @data(   ("ab","Search term minimum length is 3 characters"),("abc","No products were found that matched your criteria.")         )
    @unpack
    def test_arama_uyari_verir(self, kelime, beklenen_mesaj):
        self.driver.get("https://demowebshop.tricentis.com/")
        # simdi arama_sayfasi ndaki methodlara ulasabilmek icin AramaSayfasi class indan bir obje olusturacag#
        arama=AramaSayfasi(self.driver)
        arama.arama_yap(kelime)
        mesaj = arama.arama_uyari_mesajini_ver()

        assert mesaj==beklenen_mesaj
        #burada ddt yi yukledik terminalden
        #






