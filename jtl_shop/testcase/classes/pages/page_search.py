from jtl_shop.core.object_provider import ObjectProvider
from jtl_shop.core.base_jtl_shop import BaseJtlShop

#--
#...
#--

class PageSearch(BaseJtlShop):
    
    def __init__(self) -> None:
        self.objects = ObjectProvider()(__file__.replace('.py','.json', -1))

#--
#...
#--

    def sample(self)->None:
        print(self.find_elemnts(self.objects.product_waraper))
        
