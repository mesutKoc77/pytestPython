import pytest
import softest

from pages.anasayfa import Anasayfa


@pytest.mark.usefixtures("setup")
class TestHomepage(softest.TestCase):
    #dikkat edilirse her bir anasayfa page ini kullanirken asagidaki test_ fonksiyonlari anasayfa degiskenini
    # cagiriyor. mesela ilk testte cagirdik simdi de ikincisinde cagiriyoruz. Dolayisiyla AnaSayfa class ini
    # fixture olrak belirler ve kullanacak test_ fonksiyonuna atarsak test calismadan once bir anasayfa nesnesi
    # olusturacak.#

    #simdi bir bunun icin bir fixture olusturalim
    @pytest.fixture(autouse=True) # yani bu class in icindeki her bir test fonksiyonu, autouse=True yazilmasiyla
    #Anasayfa class indan olusan bir nesne olusturarak yoluna devam edecek.
    def class_setup(self):
        self.anasayfa = Anasayfa(self.driver)



    def test_top_menu_items(self):
        print("base url degeri = "+self.baseurl)
        self.driver.get(self.baseurl)
        expected_menu = ["BOOKS", "COMPUTERS", "ELECTRONICS", "APPAREL & SHOES", "DIGITAL DOWNLOADS",
                         "JEWELRY", "GIFT CARDS"]

        #anasayfa = Anasayfa(self.driver)
        actual_menu_items = self.anasayfa.ust_menu_isimlerini_liste_ver()
        for i in range(len(expected_menu)):
            assert expected_menu[i] == actual_menu_items[i]


    def test_urun_ismine_tiklar_ve_urun_sayfasi_acilir(self):
        self.driver.get(self.baseurl)
        #anasayfa = Anasayfa(self.driver)#buraya driver i gecmem gerekiyor ki o sayfada ilgili
        #islemleri yapabilelim.
        # urun_detay_sayfasi = UrunDetaySayfasi(self.driver)

        #eger anasayfadaki islemler ile ben bir baska sayfaya
        #geciyorsam bu drumda gecilen sayfanin nesnesi de anasayfadaki ilgili fonksiyonda olusturulabilir.


        #burada birkac daha nesne olusturmak istedgimizde, yine diger class lari cagirmak ve burada altalta
        #nesne olusturmak zorunda kalacagiz.

        urun_ismi = self.anasayfa.ilk_urun_ismini_ver() #buraada ilk urun ismine tikladm ve bu beni urun detay sayfasina
        #yonlendirdi. bu durum beni yeniden urun detay sayfasi iicn nesne olusturmaya zorladi. oyle bir sey
        #yapacagz ki driver in actigi yeni sayfanin otomatik nesnesi olusursa bu durumda yukaridaki gibi
        # "urun_detay_sayfasi = UrunDetaySayfasi(self.driver)" bir nesne olusturmama gerek kalmayacak.

        urun_fiyati = self.anasayfa.ilk_urun_fiyatini_ver()

        urun_detay_sayfasi = self.anasayfa.ilk_urun_ismine_tikla() # yani ilk_urun_ismine_tikla() fonksiyonu bana
        #UrunDetayDayfasi nin bir nesnesini return edecek ve ben de onu  urun_detay_sayfasi isimli variable a
        #atadim. o zaman en yukaridaki nesne ye gerek kalmadi.

        # Simdi gidecegz ilk urune tiklattik. Ve urun detay sayfasina gittik. Bunun yani ilk_urun_ismine_tikla()
        #fonksiyonunun sonuna gidecgz diyecegz ki madem sen buraya getirdin beni o halde bu sayfanin da hemen
        #bir nesnesini olustur. Ki fonksiyonun  son satirina bakabilirsin

        #yani sonuc olarak, ilgili bir test fonksiyonu bizi bir baska sayfaya yonlendiriyorsa bu durmda ilgili
        # sayfanin nesnesi return edilirse problöem de cozulmus olur.#
        urunismidetaysayfasi = urun_detay_sayfasi.urun_ismini_ver()
        urunfiyatidetaysayfasi = urun_detay_sayfasi.urun_fiyatini_ver()

        self.soft_assert(self.assertEqual, urun_ismi, urunismidetaysayfasi, "urun ismi detay sayfasinda farkli")
        self.soft_assert(self.assertEqual, urun_fiyati, urunfiyatidetaysayfasi, "urun fiyati detay sayfasinda farkli")
        self.assert_all()
        





        
