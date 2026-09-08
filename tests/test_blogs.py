import pytest

from pages.blogs import Blog


@pytest.mark.smoke
def test_blog(page):
    blog=Blog(page)
    blog.click_blog_option()

@pytest.mark.smoke
def test_bWebDev(page):
    bWebDev=Blog(page)
    bWebDev.click_blog_webDev()

@pytest.mark.smoke
def test_bUiUx(page):
    bWebDev=Blog(page)
    bWebDev.click_ux()

@pytest.mark.smoke
def test_App(page):
    bApp=Blog(page)
    bApp.click_App()

@pytest.mark.smoke
def test_AppNewWin(page):
    bApp=Blog(page)
    bApp.click_App_NewWin()

@pytest.mark.smoke
def test_Bgraph(page):
    bApp=Blog(page)
    bApp.click_Bgraph()