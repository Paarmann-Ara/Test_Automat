import unittest
from jtl_shop.testcase.classes.common.jtl_shop_explprer_manager import JtlShopExplprerManager
   
# --
# ...
# --

class JtlShopExplorerClose(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_close_browser(self):
        assert JtlShopExplprerManager().close_browser()

    def tearDown(self) -> None:
        pass