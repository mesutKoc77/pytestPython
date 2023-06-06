import pytest

from pages.anasayfa import Anasayfa
from pages.urun_detay_sayfasi import UrunDetaySayfasi


@pytest.mark.usefixtures("setup")
class TestHomepage:
    def test_top_menu_items(self):
        expected_menu = ["BOOKS", "COMPUTERS", "ELECTRONICS", "APPAREL & SHOES", "DIGITAL DOWNLOADS",
                         "JEWELRY", "GIFT CARDS"]

        anasayfa = Anasayfa(self.driver)
        actual_menu_items = anasayfa.ust_menu_isimlerini_liste_ver()
        for i in range(len(expected_menu)):
            assert expected_menu[i] == actual_menu_items[i]

    def test_urun_ismine_tiklar_ve_urun_sayfasi_acilir(self):
        self.driver.get("https://demowebshop.tricentis.com/")
        anasayfa = Anasayfa(self.driver)
        urun_detay_sayfasi = UrunDetaySayfasi(self.driver)

        urun_ismi = anasayfa.ilk_urun_ismini_ver()
        urun_fiyati = anasayfa.ilk_urun_fiyatini_ver()
        anasayfa.ilk_urun_ismine_tikla()
        urunismidetaysayfasi = urun_detay_sayfasi.urun_ismini_ver()

        urunfiyatidetaysayfasi = urun_detay_sayfasi.urun_fiyatini_ver()
        assert urun_ismi == urunismidetaysayfasi
        assert urun_fiyati == urunfiyatidetaysayfasi
