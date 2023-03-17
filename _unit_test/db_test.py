from db.SQLServer.SQL_connection import SQLConnection
from db.config.db_config import DBConfig
from db.SQLServer.SQL_execute import SQLExecute

db_config_dictionary = DBConfig().instance

connection = SQLConnection(driver=db_config_dictionary('Driver'), host=db_config_dictionary('Host'), database=db_config_dictionary('Database'), user_name=db_config_dictionary('UserName'), password=db_config_dictionary('Password'), is_use_default=False).instance
result = SQLExecute(connection, db_command = 'DB_TestMeRestore').execute_dbcommand()

# --
# ...
# --

connection = SQLConnection(is_use_default = True).instance
result = SQLExecute(connection, db_command = 'DB_TestMeRestore').execute_dbcommand()

# --
# ...
# --

connection = SQLConnection(is_use_default = True).instance
result = SQLExecute(connection, command = 'USE eazybusiness;SET NOCOUNT ON; SELECT * FROM dbo.tRMGrund').execute_command()