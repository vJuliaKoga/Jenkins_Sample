from playwright.sync_api import Page
import pytest


class TestHotelPlanisphere(object):

    @pytest.fixture(scope="function", autouse=True)
    def page_fixture(self, page: Page):
        self.page = page
        yield
        self.page.close()

    def test_change_all_params(self):
        self.page.goto("https://hotel.testplanisphere.dev/ja/reserve.html?plan-id=0")
