class cDescriptor:
    def __init__(self, Value=None, Name='', Condition=True) -> None:
        self.Value = Value
        self.Name = Name
        self.Condition = Condition

# --
# ...
# --

    def __get__(self, obj, objtype):
        if self.Condition:
            return self.Value
# --
# ...
# --

    def __set__(self, obj, Value) -> None:
        if self.Condition:
            self.Value = Value
