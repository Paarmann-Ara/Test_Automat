from loger.loging.log import Log

# --
# ...
# --


class LogProvider:

    def __init__(self, template='Pipeline', config='Pipeline') -> None:
        self.WRITE = Log().instance.Write
        
        self.INFO = Log(template='Pipeline', config='Pipeline').instance.Info
        self.ERROR = Log(template='Error', config='Error').instance.Error
        self.CUSTOMLOG = Log(template=template, config=config).instance.Error


LogHandler()