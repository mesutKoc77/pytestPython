import pytest

def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def bolme(a, b):
    return a/b

def carpma(a, b):
    return a * b
@pytest.mark.smoke
@pytest.mark.elma
def test_toplamaTesti():
    assert toplama(2,2)==4
@pytest.mark.elma
@pytest.mark.armut
def test_cikarmaTesti():
    assert cikarma(4,1)==3
@pytest.mark.elma
def test_bolmeTesti():
    assert bolme(20,10)==2
@pytest.mark.xfail
def test_carpmaTesti():
    assert carpma(2,8)==15


