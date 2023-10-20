from jtl_shop.testcase.classes.common.explprer_manager import ExplprerManager

# --
# ...
# --

class JtlShopPyTest_ExplorerManager():
    site_adress = "https://2-jtl-shop-p-a-7acf6a8f.docker.jtl-software.de"

    @classmethod
    def run_browser(cls):
        assert ExplprerManager(site_adress=cls.site_adress).run_browser()
        
    @classmethod
    def close_browser(cls):
        assert ExplprerManager(site_adress=cls.site_adress).close_browser()