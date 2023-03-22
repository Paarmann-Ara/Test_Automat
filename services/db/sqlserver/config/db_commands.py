from config_dictionary.base_dictionary import BaseDictionary
from services.db.sqlserver.config.db_commmands_dictionary import DBCommmandDictionary


# --
# ...
# --

class DBCommand(BaseDictionary):
        @classmethod
        def get_dictionary(cls, **kwarg) -> dict:
                print(f'DBCommand{__name__}')
                return DBCommmandDictionary(**kwarg)()