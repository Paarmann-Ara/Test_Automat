from jtl_shop.core.object_provider import ObjectProvider
from jtl_shop.core.base_jtl_shop import BaseJtlShop

#--
#...
#--

class PageHome(BaseJtlShop):
    
    def __init__(self) -> None:
        self.objects = ObjectProvider()(__file__.replace('.py','.json', -1))

#--
#...
#--

    def sample(self)->None:
        self.open("https://2-jtl-shop-p-a-7acf6a8f.docker.jtl-software.de/")
        self.set_text(self.objects.txbSearch, "Gürtel", IsUseKey = True, IsEnter = True)        