from repository_and_config.base_repository import BaseRepository
from services.disk.json.json_manager import JSONManager
import CONSTS


# --
# ...
# --

class EmailConfig(BaseRepository):
    @classmethod
    def get_dictionary(cls, *args) -> dict:
        json = JSONManager().instance
        print(__name__)
        return json.operation(CONSTS.CONFIG_JSON)[__name__]