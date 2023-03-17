from repository_and_config.base_dictionary import BaseRepository
from services.disk.json.json_manager import JSONManager
import CONSTS


# --
# ...
# --

class EmailConfig(BaseRepository):
    @classmethod
    def get_dictionary(cls, *args) -> dict:
        json = JSONManager().instance
        return json.operation(CONSTS.ROOT_DIR )[__name__.split(".")[0]]