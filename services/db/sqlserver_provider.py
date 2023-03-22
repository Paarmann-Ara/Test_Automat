from services.log_.log_provider import LogProvider
from services.db.sqlserver.core.sql_server_connection import SqlserverConnection

class SqlserverProvider:
    def __init__(self) -> None:
        self.log_info_class = LogProvider().info_instance
        self.log_error_class = LogProvider().error_instance
        
        self.sqlserver_connection = SqlserverConnection(log_info_class=self.log_info_class, log_error_class=self.log_error_class).instance