from repository_and_config.base_dictionary import BaseRepository
from services.disk.json.json_manager import JSONManager
import CONSTS

# --
# ...
# --

class DriverConfig(BaseRepository):
    @classmethod
    def get_dictionary(cls, *args) -> dict:
        json = JSONManager().instance
        return json.operation(CONSTS.CONFIG_JSON)[__name__.split(".")[0]]