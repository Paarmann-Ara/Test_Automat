from typing import Any
from services.db.sqlserver.core.base_db import BaseDB
from services.db.sqlserver.config.db_config import DBConfig
import pyodbc

#--
#...
#--


class SqlserverConnection(BaseDB):
    
#--
#...
#--

    @classmethod
    def create_connection_string(cls, driver: str = '', host: str = '', database: str = '', user_name: str = '', password: str = '', is_use_default: bool = True, **kwarg) -> str:
        
        try:
            
            if is_use_default:
                db_dictionary = DBConfig().instance.dictionary

                driver = db_dictionary['driver']
                host = db_dictionary['host'].replace('/','\\')
                database = db_dictionary['database']
                username = db_dictionary['username']
                password = db_dictionary['password']
                    
            return f"""DRIVER={{{driver}}};server={host};database={database};trusted_connection=yes;uid={username};pwd={password};"""
        
        except Exception as exp:
            cls.error(f"{__file__}-{__name__}: {str(exp)}")

#--
#...
#--

    @classmethod
    def get_connection(cls, connection_string: str) -> Any:
        
        try:
            
            return pyodbc.connect(connection_string, autocommit=True)
        
        except Exception as exp:
            cls.error(f"{__file__}-{__name__}: {str(exp)}")