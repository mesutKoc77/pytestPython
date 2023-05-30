import pytest

windowsmu="evet"
def cevre_hesaplama(a,b,c):
    return a+b+c
def ucgenalanhesaplama(taban, yukseklik):
    return taban*yukseklik/2



@pytest.mark.skip(reason="henuz tamamlanmadi")
def test_ucgenCevresi():
    print("ucgencevresutesti")
    assert 10==cevre_hesaplama(7,3,0)
@pytest.mark.skipif (windowsmu=="evet", reason="windows olmamali")
def test_ucgenAlanHesapla():
    print("yazdi mi")
    assert 5==ucgenalanhesaplama(5,2)
