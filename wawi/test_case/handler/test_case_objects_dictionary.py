from repository_and_config.base_dictionary import BaseRepository
from services.disk.json.json_manager import JSONManager
import CONSTS

# --
# ...
# --

class TestCaseObjectDictionary(BaseRepository):
    @classmethod
    def get_dictionary(cls, *arg) -> dict:
        
        json = JSONManager().instance
        test_case_objects_dictionary = json.operation(CONSTS.CONFIG_JSON)['test_case_objects']['test_case_objects_dictionary']
        objects_dictionary = json.operation(test_case_objects_dictionary + '\\' + arg[0] + '.json')
        
        return objects_dictionary
    