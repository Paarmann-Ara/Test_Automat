from config.base_dictionary import BaseRepository
from db.config.db_commmands_dictionary import DBCommmandDictionary


# --
# ...
# --

class DBCommand(BaseRepository):
        @classmethod
        def get_dictionary(cls, **kwarg) -> dict:
                return DBCommmandDictionary(**kwarg)()