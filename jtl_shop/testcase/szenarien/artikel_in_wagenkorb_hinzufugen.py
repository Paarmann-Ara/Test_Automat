from jtl_shop.testcase.classes.common.cookies import Cookies
from jtl_shop.testcase.classes.pages.page_home.page_home import PageHome
from jtl_shop.testcase.classes.pages.page_search.page_result_search import PageResultSearch
from jtl_shop.testcase.classes.common.jtl_shop_explprer_manager import JtlShopExplprerManager

# --
# ...
# --


class ArtikelInWagenkorbHinzufugen:
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

        self.artikel = "Gürtel"
        self.site_adress = "https://2-jtl-shop-p-a-7acf6a8f.docker.jtl-software.de/search/?qs=G%C3%BCrtel"

# --
# ...
# --

    def setUp(self) -> None:
        pass

    def test_000_run_explorer(self):
        assert JtlShopExplprerManager(site_adress=self.site_adress).run_browser()
               
    def test_100_get_all_cookies(self):
        assert isinstance(Cookies().get_alle_cookies(), list)
        
    def test_200_delete_all_cookies(self):
        assert Cookies().alle_cookies_loschen()
        
    def test_300_akzeptiren_cookies(self):
        assert Cookies().akzeptiren_cookies()
        
    def test_400_textbox_search_item(self):
        assert PageHome().textbox_search_item(text=self.artikel)
        
    def test_500_artikel_page_besuchen():
        assert PageResultSearch().present_page_of_first_item_nach_suchen()
        
        
        

    def test_1000_close_browser(self):
        assert JtlShopExplprerManager().close_browser()

    def tearDown(self) -> None:
        pass
