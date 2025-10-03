from playwright.sync_api import Page, expect
import pytest

class TestHotelPage:

    def test_reserve_page_title(self, page: Page):
        url = "https://hotel.testplanisphere.dev/ja/reserve.html?plan-id=0"
        page.goto(url)

        # ページタイトルを取得
        title = page.title()
        print(f"[INFO] ページタイトル取得: {title}")

        # アサーション
        assert title == "Planisphere Hotel", f"タイトルが一致しません: {title}"
        print("[SUCCESS] タイトルが 'Planisphere Hotel' と一致しました。")
