from log_all.log import Log

INFO = Log(template='Pipeline',config='Pipeline').instance.Info
ERROR = Log(template='Error',config='Error').instance.Error