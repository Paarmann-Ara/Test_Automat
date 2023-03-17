from base.base_repository import BaseRepository
from disk.json.json_manager import JSONManager
import CONSTS


# --
# ...
# --

class LogConfig(BaseRepository):
    @classmethod
    def get_dictionary(cls, *args) -> dict:
        json = JSONManager().instance
        return json.operation(CONSTS.CONFIG_JSON)[__name__.split(".")[-1]]