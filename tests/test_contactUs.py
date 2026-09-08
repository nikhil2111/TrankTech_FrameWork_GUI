import pytest

from pages.contactUs import ContactUs


@pytest.mark.smoke
def test_ContactUs_Form(page):
    form=ContactUs(page)
    form.contact_FormFill()