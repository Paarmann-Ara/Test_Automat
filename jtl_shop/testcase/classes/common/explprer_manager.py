from jtl_shop.core.object_provider import ObjectProvider
from jtl_shop.core.base_jtl_shop import BaseJtlShop

# --
# ...
# --


class ExplprerManager(BaseJtlShop):
    def __init__(self, site_adress: str = '') -> None:
        self.objects = self.get_objects()
        self.site_adress = site_adress

# --
# ...
# --

    def get_objects(self) -> str:
        return ObjectProvider()(__file__.replace('.py', '.json', -1))

# --
# ...
# --

    def run_browser(self) -> bool:
        return self.get(self.site_adress)

# --
# ...
# --

    def close_browser(self) -> bool:
        return self.quit()

# --
# ...
# --

    def forward_browser(self) -> bool:
        return self.forward()

# --
# ...
# --

    def backward_browser(self) -> bool:
        return self.instance.backward()
