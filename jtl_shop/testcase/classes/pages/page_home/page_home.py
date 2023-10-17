from jtl_shop.core.object_provider import ObjectProvider
from jtl_shop.core.base_jtl_shop import BaseJtlShop

#--
#...
#--

class PageHome(BaseJtlShop):
    def __init__(self) -> None:
        self.objects = self.get_objects()
        
# --
# ...
# --
    
    def get_objects(self) -> str:
        return ObjectProvider()(__file__.replace('.py','.json', -1))

#--
#...
#--

    def textbox_search_item(self, text:str = "Gürtel")->None:
        return self.set_text(self.objects.txbSearch, text, IsUseKey = True, IsEnter = True)
        