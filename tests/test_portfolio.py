import pytest

from pages.portfolio import Portfolio

@pytest.mark.smoke
def test_PortNewWindow(page):
    newWindow=Portfolio(page)
    newWindow.click_PortNewWindow()

@pytest.mark.smoke
def test_webDev(page):
    webD=Portfolio(page)
    webD.click_webDev()

@pytest.mark.smoke
def test_ux(page):
    uiux=Portfolio(page)
    uiux.click_ux()

@pytest.mark.smoke
def test_App(page):
    appD=Portfolio(page)
    appD.click_App()

@pytest.mark.smoke
def test_graph(page):
    graph=Portfolio(page)
    graph.click_graph()