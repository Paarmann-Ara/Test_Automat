from config_dictionary.base_dictionary import BaseDictionary
from services.disk.json.json_manager import JSONManager
import CONSTS

# --
# ...
# --

class TestcaseObjectDictionary(BaseDictionary):

    @classmethod
    def get_dictionary(cls, **kwarg) -> dict:
        json = JSONManager().instance
        
        if 'dictionary_fulladress' in kwarg:
            return json.operation(f'{CONSTS.ROOT_DIR}//{kwarg["dictionary_fulladress"]}')
            
        else:        
            return json.operation(CONSTS.CONFIG_JSON)[__name__]