from jtl_shop.core.object_provider import ObjectProvider
from jtl_shop.core.base_jtl_shop import BaseJtlShop

#--
#...
#--

class PageResultSearch(BaseJtlShop):
    def __init__(self) -> None:
        self.objects = self.get_objects()
        self.product_list = []
    
# --
# ...
# --
    
    def get_objects(self) -> str:
        return ObjectProvider()(__file__.replace('.py','.json', -1))

#--
#...
#--

    def label_suche_nach_text(self)->None:
        suche_nach_text = self.find_element(self.objects.suche_nach).text
        print(suche_nach_text)
        return suche_nach_text
#--
#...
#--

    def items_nach_suchen(self)->None:
        
        print(id(self.driver))
        self.set_driver(self.find_element(self.objects.product_list))
        print(id(self.driver))
        temp_selenium_driver_product_list = self.find_elements(*self.objects.product_item_in_product_list.popitem())

        for temp_selenium_driver_product in temp_selenium_driver_product_list:
            print(temp_selenium_driver_product.text)
            self.product_list.append(temp_selenium_driver_product.text)
            
        return self.product_list


        
        
        temp_selenium_driver_products = self.find_element(self.objects.product_list)
        temp_selenium_driver_product_list = temp_selenium_driver_products.find_elements(*self.objects.product_item_in_product_list.popitem())
        
        for temp_selenium_driver_product in temp_selenium_driver_product_list:
            print(temp_selenium_driver_product.text)
            self.product_list.append(temp_selenium_driver_product.text)
            
        return self.product_list
    
#--
#...
#--

    def present_page_of_first_item_nach_suchen(self)->None:
        temp_selenium_driver_products = self.find_element(self.objects.product_list)
        temp_selenium_driver_product_list = temp_selenium_driver_products.find_elements(*self.objects.product_hyperlink_in_product_list.popitem())
        self.delay(2)
        temp_selenium_driver_product_list[0].click()
        return True
    
#--
#...
#--

    def present_page_item_nach_suchen(self, item)->None:
        temp_selenium_driver_products = self.find_element(self.objects.product_list)
        temp_selenium_driver_product_list = temp_selenium_driver_products.find_elements(*self.objects.product_item_in_product_list.popitem())
        
        for temp_selenium_driver_item in temp_selenium_driver_product_list:
            if temp_selenium_driver_item.text == item:
                self.delay(3)
                temp_selenium_driver_item.click()
                self.delay(3)
        
        return True