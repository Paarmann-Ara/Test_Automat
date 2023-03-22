from config_dictionary.base_dictionary import BaseDictionary
from services.disk.json.json_manager import JSONManager
import CONSTS


# --
# ...
# --

class DBConfig(BaseDictionary):
    @classmethod
    def get_dictionary(cls, *args) -> dict:
        json = JSONManager().instance
        return json.operation(CONSTS.CONFIG_JSON)[__name__]