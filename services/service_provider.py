from services.db.sqlserver_provider import SqlserverProvider
from services.disk.json.json_manager import JSONManager
from services.disk.xml.xml_manager import XMLManager
from services.log_.log_provider import LogProvider
from services.log_.stack_context_provider import StackContextProvider

class ServiceProvider:
    def __init__(self) -> None:
        db_connection = SqlserverProvider().sqlserver_connection
        json = JSONManager().instance
        xml = XMLManager().instance
        info = LogProvider(template='Pipeline',config='Pipeline').info_instance
        error = LogProvider(template='error',config='error').error_instance
        stack = StackContextProvider().stack