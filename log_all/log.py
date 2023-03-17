from typing import Any
from disk.file.file_manager import FileManager
from log_all.config.log_config import LogConfig
from base.base_log import BaseLog
from log_all.templates.log_template_dictionary import LogTemplateDictionary

#--
#...
#--


class Log(BaseLog):
    def __init__(self, **kwarg) -> None:
        
        try:
            
            #remove error for IDE
            self.log_config_dictionary = self.log_config_dictionary
            
            #aliance for short writing
            self.Info = self.set_information_for_log_file
            self.Error = self.set_information_for_log_file
            self.Write = self.write_in_log_file
            
            #create instance for file operation
            self.file_manager = FileManager().instance
            self.info_message = ['\n']

            #set log config        
            self.log_file = self.log_config_dictionary['Directory'] + self.log_config_dictionary['FileName']
            self.number_of_log_in_batch = int(self.log_config_dictionary['NumberOfLogInBatch'])
            self.is_show_in_consoule = bool(self.log_config_dictionary['ShowInConsoule'])
            
        except Exception as exp:
            print(__name__ + str(exp))
        
#--
#...
#--

    @classmethod
    def get_template_dictionary(cls):
            return LogTemplateDictionary()()
        
#--
#...
#--

    @classmethod
    def get_log_config_dictionary(cls):
            return LogConfig().instance.dictionary

#--
#...
#--
    
    def set_information_for_log_file(self, message):

        try:
            
            #print message on screen
            if self.is_show_in_consoule:
                temp = f"import datetime\nprint({self.log_template})"
                exec(temp, {'message': message})

            #compile message and template
            temp = f"""import datetime;temp ={self.log_template}; f = open("temp.txt", "w"); f.write(str(temp[0] + temp[1]))"""
            exec(temp, {'message': message})
            
            #prepaire message
            message = self.file_manager.operation('r', 'temp.txt')
            
            #send message to write in file
            self.info_message.append(message)
            if len(self.info_message) > self.number_of_log_in_batch:
                self.write_in_log_file()
                
        except Exception as exp:
            print(__name__ + str(exp))

#--
#...
#--

    def write_in_log_file(self):
        
        try:
            
            self.file_manager.operation('a', self.log_file, '\n'.join(self.info_message))
            self.info_message.clear()
            self.info_message.append('\n')
            
        except Exception as exp:
            print(__name__ + str(exp))