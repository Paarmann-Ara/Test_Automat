from typing import Any
from abc import ABC, abstractmethod


# --
# ...
# --
    
class BaseEmailTemplate(ABC):
    def __init__(self, **kwarg: Any) -> None:
        pass
    
# --
# ...
# --
   
    instance = None
    def __new__(cls, *args, **kwarg: Any):
        if not hasattr(cls, 'instance') or not cls.instance:
            cls.instance = super().__new__(cls)
            
            body = cls.clear_body(**kwarg)
            cls.instance.template = {'html': cls.get_template(body), 'body' : body}
                   
        return cls.instance
    
# --
# ...
# --
    
    @classmethod
    def get_template(cls, **kwarg) -> str:
        return ''
    
# --
# ...
# --

    @classmethod
    def clear_body(cls, **kwarg) -> str:
        body = kwarg['body']
        body = body.replace("\n", "<br>\n")
        body = body.replace(" ", "&nbsp;")
        return body
    
# --
# ...
# --

    def __call__(self) -> str:
        return self.template