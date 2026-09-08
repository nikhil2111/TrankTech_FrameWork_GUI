
import pytest

from pages.verticals import vertical

##----Vertical-Trading options:Object of vertical calls and called method
@pytest.mark.smoke
def test_trading(page):
    trade = vertical(page)
    trade.click_trading_option()

##----Vertical-Retail options:Object of vertical calls and called method
@pytest.mark.smoke
def test_eComm(page):
    ecom=vertical(page)
    ecom.click_Ecom_option()

##----Vertical-Healthcare options:Object of vertical calls and called method
@pytest.mark.smoke
def test_heath(page):
    hlt=vertical(page)
    hlt.click_health_option()

##----Vertical-Fintech options:Object of vertical calls and called method
def test_fintech(page):
    fin=vertical(page)
    fin.click_fintect_option()

##----Vertical-Custom options:Object of vertical calls and called method
def test_custom(page):
    custom=vertical(page)
    custom.click_custom_option()