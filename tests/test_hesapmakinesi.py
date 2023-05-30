import pytest

def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def bolme(a, b):
    return a/b

def carpma(a, b):
    return a * b

def test_toplamTesti():
    assert toplama(2,2)==4

def test_cikar():
    assert cikarma(4,1)==3
def test_bolme():
    assert bolme(20,10)==2


@pytest.mark.xfail
def test_carpma():
    assert carpma(2,8)==15



