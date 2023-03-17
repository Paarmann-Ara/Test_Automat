from llogingimport log_me
from db.config.db_commands import DBCommand
from wawi.config.wawi.wawi_config import AQCConfig
import time
from typing import Any

#--
#...
#--


class SQLExecute():
    def __init__(self, connection, db_command = '', command = '', is_use_default = True, **dbcommandskw: dict) -> None:
        
        log_me.INFO(__name__)
        
        try:
            
            self.command = command
            self.db_command = db_command

            self.connection = connection.connection
            self.cursor = self.connection.cursor()
            
            if db_command and is_use_default:
                aqc_config_dictionary = AQCConfig().instance
                testme_db_folder = aqc_config_dictionary('TestMeDBFolder')
                testme_db = aqc_config_dictionary('TestMeDB')
                testme_version_folder = aqc_config_dictionary('TestMeVersionFolder')
                
                if db_command: 
                    self.db_command = DBCommand(testme_db_folder=testme_db_folder, testme_db=testme_db, testme_version_folder=testme_version_folder).instance(db_command)
        
        except Exception as exp:
            log_me.ERROR(__name__ + str(exp))

#--
#...
#--

    def execute_dbcommand(self) -> Any:
        
        log_me.INFO(__name__)
        
        try:
          
            result:bool = True
            _ = 0
            
            log_me.INFO(self.db_command)
            
            self.cursor.execute(self.db_command)
            log_me.INFO(*list(map(lambda x: x, self.cursor.messages)))
            
            while self.cursor.nextset():
                log_me.INFO(f'I am yet {_} sec in SQLExecute...' )
                time.sleep(5)
                _ += 5
    
        except Exception as exp:
            result = False
            log_me.ERROR(__name__ + str(exp))
            
        finally:
            self.cursor.close()
            self.connection.close()
            return result
                    
#--
#...
#--        

    def execute_command(self):
        
        log_me.INFO(__name__)
        
        try:
            
            result = {}
            commands = self.command.split(";")
            
            for command in commands:
                
                try:
                    
                    log_me.INFO(command)
                    self.cursor.execute(command)

                    log_me.INFO(*list(map(lambda x: x, self.cursor.messages)))
                        
                    row = self.cursor.fetchone()
                    result = dict(zip(list(map(lambda x: x[0], row.cursor_description)), row))

                except Exception as exp:
                    log_me.ERROR(__name__ + str(exp))

        except Exception as exp:
            log_me.ERROR(__name__ + str(exp))
            result = 'DB Fehler'
                
        finally:
            self.cursor.close()
            self.connection.close()
            return result