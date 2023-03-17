from log_all.log import Log

INFO = Log(template='Pipeline',config='Pipeline').instance
ERROR = Log(template='Error',config='Error').instance

INFO.Info('Log_Info_0')
INFO.Info('Log_Info_1')
INFO.Info('Log_Info_1')
INFO.Info('Log_Info_3')

ERROR.Error('Log_Error_0')
ERROR.Error('Log_Error_1')

INFO.Info('Log_Info_3')
INFO.Info('Log_Info_2')
INFO.Info('Log_Info_2')
INFO.Info('Log_Info_3')
INFO.Info('Log_Info_3')

INFO.Write()

INFO.Info('Log_Info_23')
INFO.Info('Log_Info_33')
INFO.Info('Log_Info_33')

INFO.Write()