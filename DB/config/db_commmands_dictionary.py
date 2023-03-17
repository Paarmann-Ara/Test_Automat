class DBCommmandDictionary:
    def __init__(self, **kwargs) -> None:
        
        self.listview_name = kwargs.get('listview_name') if 'listview_name' in kwargs else ''
        self.node_name = kwargs.get('node_name') if 'node_name' in kwargs else ''
        self.column_name = kwargs.get('column_name') if 'column_name' in kwargs else ''
        self.time_metric = kwargs.get('time_metric') if 'time_metric' in kwargs else ''
        self.log_info = kwargs.get('log_info') if 'log_info' in kwargs else ''
        
        self.testme_db_folder = kwargs.get('testme_db_folder') if 'testme_db_folder' in kwargs else ''
        self.testme_db = kwargs.get('testme_db') if 'testme_db' in kwargs else ''
        self.testme_version_folder = kwargs.get('testme_version_folder') if 'testme_version_folder' in kwargs else ''
        
        self.default_db_name = 'eazybusiness'
        self.default_backup_adress = 'C:\Mad-Grb\Apps\WAWi.BAK'
        self.default_db_data_name = 'eazybusiness'
        self.default_db_data_adress = 'C:\Program Files\Microsoft SQL Server\MSSQL14.JTLWAWI\MSSQL\DATA\eazybusiness.mdf'
        self.default_db_log_name = 'eazybusiness_log'
        self.default_db_log_adress = 'C:\Program Files\Microsoft SQL Server\MSSQL14.JTLWAWI\MSSQL\DATA\eazybusiness_log.ldf'
        
# --
# ...
# --
        
    def __call__(self) -> dict:
        self.dictionary = {
            'STANDARD': f""" USE MASTER;SELECT DATABASEPROPERTYEX ('eazybusiness', 'STATUS') """,
            'AC': f""" USE MASTER;SELECT user_access FROM sys.databases WHERE name = 'eazybusiness' """,
            'MU': f""" USE MASTER;DECLARE @kill varchar(8000) = ''; SELECT @kill = @kill + 'kill' + CONVERT(varchar(5), session_id) + \';\' FROM sys.dm_exec_sessions WHERE database_id  = db_id(\'eazybusiness\') EXEC(@kill);ALTER DATABASE eazybusiness SET MULTI_USER """,
            'Del': f""" USE AQC;TRUNCATE TABLE ListViewCheck """,
            'LogTime': f"""USE AQC;INSERT INTO [ListViewCheck] ([ListViewName], [Node], [Spalte], [Time], [Loginfo]) VALUES ('{self.listview_name}', '{self.node_name}', '{self.column_name}', '{self.time_metric}', '{self.log_info}') """,
            'DB_Restore': f""" USE MASTER;ALTER DATABASE {self.default_db_name} SET SINGLE_USER WITH ROLLBACK IMMEDIATE; RESTORE DATABASE {self.default_db_name} FROM DISK = '{self.default_backup_adress}' WITH MOVE '{self.default_db_data_name}' TO '{self.default_db_data_adress}', MOVE '{self.default_db_log_name}' TO '{self.default_db_log_adress}', REPLACE, RECOVERY, STATS = 10;ALTER DATABASE {self.default_db_name} SET MULTI_USER """,
            'DB_MailRestore': f""" USE MASTER;ALTER DATABASE {self.default_db_name} SET SINGLE_USER WITH ROLLBACK IMMEDIATE; RESTORE DATABASE {self.default_db_name} FROM DISK = 'C:\Mad-Grb\Apps\DB.BAK' WITH MOVE '{self.default_db_data_name}' TO '{self.default_db_data_adress}', MOVE '{self.default_db_log_name}' TO '{self.default_db_log_adress}', REPLACE, RECOVERY, STATS = 10;ALTER DATABASE {self.default_db_name} SET MULTI_USER """,
            'DB_TestMeRestore': f""" USE MASTER;ALTER DATABASE {self.default_db_name} SET SINGLE_USER WITH ROLLBACK IMMEDIATE;RESTORE DATABASE {self.default_db_name} FROM DISK = '{self.testme_db_folder}\{self.testme_db}' WITH MOVE '{self.default_db_data_name}' TO '{self.default_db_data_adress}', MOVE '{self.default_db_log_name}' TO '{self.default_db_log_adress}', REPLACE, RECOVERY, NOUNLOAD;ALTER DATABASE {self.default_db_name} SET MULTI_USER """,
            'DB_TestMeBackup': f""" USE MASTER;ALTER DATABASE {self.default_db_name} SET SINGLE_USER WITH ROLLBACK IMMEDIATE; BACKUP DATABASE {self.default_db_name} TO DISK = '{self.testme_version_folder}/DB.bak' WITH STATS = 10;ALTER DATABASE {self.default_db_name} SET MULTI_USER """,
            'Error': f""" USE AQC;INSERT INTO [Errors] ([Loginfo]) VALUES ('{self.log_info}') """,
        }
        
        return self.dictionary
