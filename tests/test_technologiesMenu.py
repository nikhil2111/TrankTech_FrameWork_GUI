import pytest

from pages.technology import Technologies

##----Technologies-EComm option: Object of Technologies calls and called method
@pytest.mark.smoke
def test_eComm(page):
    ecom=Technologies(page)
    ecom.click_Ecom_option()

##----Technologies-MobileApp option: Object of Technologies calls and called method
@pytest.mark.smoke
def test_mobApp(page):
    mApp=Technologies(page)
    mApp.click_MobileApp_option()

##-------Technologies-Artificial Intelligence option: Object of Technologies calls and called method
@pytest.mark.smoke
def test_artInt(page):
    artInt=Technologies(page)
    artInt.click_artInt()