import unittest
from jtl_shop.testcase.classes.common.jtl_shop_explprer_manager import JtlShopExplprerManager
   
# --
# ...
# --

class JtlShopExplorerRun(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_run_browser(self):
        assert JtlShopExplprerManager().run_browser()

    def tearDown(self) -> None:
        pass