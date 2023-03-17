from llogingimport log_me
from typing import Any
from db.base_db_connection import BaseDBConnection
from db.config.db_config import DBConfig
import pyodbc

#--
#...
#--


class SQLConnection(BaseDBConnection):
        
    @classmethod
    def create_connection_string(cls, driver: str = '', host: str = '', database: str = '', user_name: str = '', password: str = '', is_use_default: bool = True) -> str:
        
        log_me.INFO(__name__)
        
        try:
            
            if is_use_default:
                db = DBConfig().instance

                driver = db('Driver')
                host = db('Host')
                database = db('Database')
                user_name = db('UserName')
                password = db('Password')
                    
            return f"""DRIVER={{{driver}}};SERVER={host};DATABASE={database};trusted_connection=yes;User ID={user_name};Password={password};"""
        
        except Exception as exp:
            log_me.ERROR(__name__ + str(exp))
    
#--
#...
#--

    @classmethod
    def get_connection(cls, connection_string: str) -> Any:
        
        log_me.INFO(__name__)
        
        try:
            
            return pyodbc.connect(connection_string, autocommit=True)
        
        except Exception as exp:
            log_me.ERROR(__name__ + str(exp))