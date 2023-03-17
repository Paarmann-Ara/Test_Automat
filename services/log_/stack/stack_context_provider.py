from services.log_.stack.stack_context import StackContext

# --
# ...
# --


class StackContextProvider:
    def __init__(self, object_name='') -> None:
        self.stack = StackContext(object_name=object_name).StackOperation