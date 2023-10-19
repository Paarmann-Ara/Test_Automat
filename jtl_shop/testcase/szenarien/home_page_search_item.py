import unittest
from jtl_shop.testcase.classes.common.cookies import Cookies
from jtl_shop.testcase.classes.pages.page_home.page_home import PageHome
from jtl_shop.testcase.classes.pages.page_search.page_result_search import PageResultSearch
from jtl_shop.testcase.classes.common.jtl_shop_explprer_manager import JtlShopExplprerManager

# --
# ...
# --


class HomePageSearchItem(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

        self.such_item = "Gürtel"
        self.item_to_present_page = "Tommy"
        self.site_adress = "https://2-jtl-shop-p-a-7acf6a8f.docker.jtl-software.de/search/?qs=G%C3%BCrtel"

# --
# ...
# --

    def setUp(self) -> None:
        pass

    def test_000_run_explorer(self):
        assert JtlShopExplprerManager(site_adress=self.site_adress).run_browser()
        
    def test_010_(self):
        assert Cookies().akzeptiren_cookies()

    def test_100_textbox_search_item(self):
        assert PageHome().textbox_search_item(text=self.such_item)

    def test_200_text_suche_nach_in_result_page(self):
        assert PageResultSearch().label_suche_nach_text().index(self.such_item) > 0

    def test_300_list_items_nach_suchen_in_result_page(self):
        assert len(PageResultSearch().list_items_nach_suchen()) > 0

    def test_400_first_item_nach_suchen_in_result_page_besuchen(self):
        assert PageResultSearch().present_page_of_first_item_nach_suchen()
        
    def test_500_backward_browser(self):
        assert JtlShopExplprerManager().backward_browser()
        
    def test_600_item_nach_suchen_in_result_page(self):
        assert PageResultSearch().present_page_item_nach_suchen(self.item_to_present_page)
        
    def test_700_backward_browser(self):
        assert JtlShopExplprerManager().backward_browser()
        
    def test_800_close_browser(self):
        assert JtlShopExplprerManager().close_browser()

    def tearDown(self) -> None:
        pass
