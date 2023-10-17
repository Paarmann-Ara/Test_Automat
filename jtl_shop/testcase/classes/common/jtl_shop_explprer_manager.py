from jtl_shop.core.object_provider import ObjectProvider
from jtl_shop.core.base_jtl_shop import BaseJtlShop

#--
#...
#--

class JtlShopExplprerManager(BaseJtlShop):
    def __init__(self, site_adress=None) -> None:
        self.objects = self.get_objects()
        self.site_adress = site_adress
    
# --
# ...
# --
    
    def get_objects(self) -> str:
        return ObjectProvider()(__file__.replace('.py','.json', -1))

#--
#...
#--

    def run_browser(self)->None:
        self.open(self.site_adress)
        return True
#--
#...
#--

    def close_browser(self)->None:
        self.close()
        return True