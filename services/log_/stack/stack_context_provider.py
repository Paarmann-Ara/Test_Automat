from services.log_.stack.stack_context import StackContext

# --
# ...
# --


class StackContextProvider:
    def __init__(self) -> None:
        self.stack = StackContext().StackOperation