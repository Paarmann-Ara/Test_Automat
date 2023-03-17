from wawi.test_case.handler.test_case_objects_dictionary import TestCaseObjectDictionary


#--
#...
#-- 

class TestCaseObject:
    def __init__(self, dictionary_name: str) -> None:
        self.object_dictionary = TestCaseObjectDictionary(dictionary_name).instance
        
    def __call__(self, *args: str) -> str:
        return self.object_dictionary(args[0])