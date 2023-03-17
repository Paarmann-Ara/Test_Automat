from services.log_.loging.log import Log
from services.disk.file.file_manager import FileManager
from services.log_.config.log_config import LogConfig

# --
# ...
# --


class LogProvider:
    def __init__(self, template='Pipeline', config='Pipeline') -> None:
        
        self.file_manager_class = FileManager().instance
        self.log_config_class = LogConfig().instance.dictionary
        
        self.info_instance = Log(template='Pipeline', config='Pipeline', file_manager_class=self.file_manager_class).instance.Info
        self.error_instance = Log(template='Error', config='Error', file_manager_class=self.file_manager_class).instance.Error