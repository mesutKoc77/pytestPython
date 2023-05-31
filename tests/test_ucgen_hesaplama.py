import pytest

windowsmu="evet"
def cevre_hesaplama(a,b,c):
    return a+b+c
def ucgenalanhesaplama(taban, yukseklik):
    return taban*yukseklik/2


@pytest.fixture()
def ucgen():
    print("ucgen olustu ve fixture kullanildi ve ilgili url e gidildi")
    yield
    print("ucgeni sildim ve ana sayfaya dondum")

    #fixture ile herbir testin baslamadan once yapacaklari belirleniyor ve onun icindeki
    #method calisiyor ve en son yield ile sonlandirip istersem basa da donus saglayabilirim
    # #

def test_ucgenCevresi(ucgen):
    print("ucgencevrehesaplama")
    assert 10==cevre_hesaplama(7,3,0)

def test_ucgenAlanHesapla(ucgen):
    print("ucgen alan hesaplama")
    assert 5==ucgenalanhesaplama(5,2)
