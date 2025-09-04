import pytest
from selene import browser



@pytest.fixture()
def windows_size():
    browser.config.window_height = 1080
    browser.config.window_width = 1920


