import re
import traceback
from log_all.log import Log
from typing import Any

# --
# ...
# --


class StackContext:
    def __init__(self, object_name) -> None:

        log_config = Log(config="no_show").instance
        self.object_name = object_name
        self.no_show_moduls = log_config.log_config_dictionary["no_show_moduls"]
        self.no_show_methods = log_config.log_config_dictionary["no_show_methods"]
        
    def __str__(self) -> str:
        return self.StackOperation()
        
# --
# ...
# --
    
    def StackOperation(self)-> Any:

        try:

            Stack:Any = ''

            if self.object_name != '':
                Stack = re.search(r"([(]).+([)])", self.object_name)

            else:
                for line in traceback.format_stack()[3:]:
                    # Data = re.search("([aq:]+\w+).+([, line ]+\d+).+([, in ]+\w+)", line)
                    Data = re.search(r"([aq:]+\w+).+([, line ]+\d+)", line)

                    if Data:
                        Module = Data.group(1)[3:]
                        Line = Data.group(2)[1:]

                        if Module not in self.no_show_moduls:
                            Data = re.search(r"(\b, in\b.\w+)", line)
                            Method = '0'

                            if Data:
                                Method = Data.group()[5:]

                                if Method not in self.no_show_methods:
                                    Stack = Stack + ' > ' + Module + \
                                        '.' + Method + '(' + Line + ')'

            return Stack

        except Exception as exp:
            print(__file__ + ': ' + str(exp))
            