def cevre_hesaplama(a,b,c):
    return a+b+c
def ucgenalanhesaplama(taban, yukseklik):
    return taban*yukseklik/2

def test_ucgenCevresi():
    print("ucgencevresutesti")
    assert 10==cevre_hesaplama(7,3,0)

def test_ucgenAlanHesapla():
    print("yazdi mi")
    assert 7==ucgenalanhesaplama(5,2)
