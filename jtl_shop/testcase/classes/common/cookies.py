from jtl_shop.core.object_provider import ObjectProvider
from jtl_shop.core.base_jtl_shop import BaseJtlShop

#--
#...
#--

class Cookies(BaseJtlShop):
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

    def akzeptiren_cookies(self)->None:
        self.find_element(self.objects.btn_akzeptiren).click()
        return True

#--
#...
#--

    def alle_cookies_loschen(self)->None:
        return self.delete_all_cookies()

#--
#...
#--

    def get_alle_cookies(self):
        all_cookies = self.get_all_cookies()
        print(all_cookies)
        return all_cookies