from jtl_shop.core.object_provider import ObjectProvider
from jtl_shop.core.base_jtl_shop import BaseJtlShop

#--
#...
#--

class PageSearch(BaseJtlShop):
    def __init__(self) -> None:
        self.objects = self.get_objects()
        
        print(f"{__class__.__name__}:{id(self.instance)}")
    
# --
# ...
# --
    
    def get_objects(self) -> str:
        return ObjectProvider()(__file__.replace('.py','.json', -1))

#--
#...
#--

    def sample(self)->None:
        print(self.find_elemnts(self.objects.suche_nach))
        
