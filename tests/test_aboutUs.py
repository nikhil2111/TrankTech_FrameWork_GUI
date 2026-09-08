import pytest

from pages.aboutUs import AboutUs


@pytest.mark.smoke
def test_aboutUs(page):
    aboutUs=AboutUs(page)
    aboutUs.click_AboutUs()