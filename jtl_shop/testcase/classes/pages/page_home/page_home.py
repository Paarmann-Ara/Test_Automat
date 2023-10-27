from jtl_shop.testcase.classes.pages.page_home.form_login import FormLogin
from jtl_shop.testcase.classes.common.explprer_manager import ExplprerManager
from jtl_shop.core.object_provider import ObjectProvider
from jtl_shop.core.base_jtl_shop import BaseJtlShop


class PageHome(BaseJtlShop):
    def __init__(self) -> None:
        self.elements = self.get_elements()

# --
# ...
# --

    def get_elements(self) -> str:
        return ObjectProvider()(__file__.replace('.py', '.json', -1))

# --
# ...
# --

    def get_all_menus_name(self) -> list:
        _, menus_name = self.gat_menu_item(self.elements.header_menu)
        return menus_name

# --
# ...
# --

    def get_all_menus_item(self) -> list:
        _, menus_item = self.gat_menu_item(self.elements.header_menu)
        return menus_item

# --
# ...
# --

    def get_all_kategories_name(self) -> list:
        _, kategories_name = self.gat_navbar_item(self.elements.nav_kategories)
        return kategories_name

# --
# ...
# --

    def get_all_kategories_element(self) -> list:
        kategories_element, _ = self.gat_navbar_item(
            self.elements.nav_kategories)
        return kategories_element

# --
# ...
# --

    def search_item_eingeben(self, text: str = "Gürtel") -> bool:
        return self.set_text(self.elements.txb_search, text=text, is_use_key=True, is_enter=True)

# --
# ...
# --

    def to_login_form(self) -> bool:
        self.click(self.elements.btn_user)


# ExplprerManager(
#     site_adress="https://2-jtl-shop-p-a-7acf6a8f.docker.jtl-software.de").run_browser()
# PageHome().to_login_form()
# FormLogin().logindata_eingeben()