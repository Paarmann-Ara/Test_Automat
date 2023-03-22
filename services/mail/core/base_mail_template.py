from typing import Any
from abc import ABC, abstractmethod


# --
# ...
# --
    
class BaseMailTemplate(ABC):
    def __init__(self, **kwarg: Any) -> None:
        pass
    
# --
# ...
# --
   
    instance: Any = None
    def __new__(cls, **kwarg: Any):
        
        if hasattr(cls, 'instance_args'):
            if cls.instance_args != kwarg:
                cls.instance = None
                
        if not hasattr(cls, 'instance') or not cls.instance:
            cls.instance = super().__new__(cls)
            
            cls.instance_args = kwarg
            
            body = cls.clear_body(**kwarg)
            cls.instance.template_object = {'template': cls.get_template(), 'mixed_html': cls.get_mixed_html_body(body), 'body' : body}
                   
        return cls.instance
    
# --
# ...
# --
    
    @classmethod
    def get_mixed_html_body(cls, body) -> str:
        return ''
    
# --
# ...
# --
    
    @classmethod
    def get_template(cls) -> str:
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