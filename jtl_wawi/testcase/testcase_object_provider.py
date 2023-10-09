from jtl_wawi.testcase.testcase_object.testcase_objects_dictionary import TestcaseObjectDictionary
from jtl_wawi.testcase.testcase_object.class_of_dictionary import ClassOfDictionary

#--
#...
#-- 

class TestcaseObjectProvider:
    def __init__(self, object_name) -> None:
        self.item = ''
        #get testcase object config from fconfig.json
        self.testcase_object_config_dictionary = TestcaseObjectDictionary().instance.dictionary
        testcase_object_directory = self.testcase_object_config_dictionary['testcase_object_directory']
        
        #get object from object dictionary
        object_file_name = f'{object_name}.json'
        
        dictionary_fulladress = f'{testcase_object_directory}//{object_file_name}'
        dictionary = TestcaseObjectDictionary(dictionary_fulladress=dictionary_fulladress).instance.dictionary
        
        #create class of object dictionary
        self.object_class = ClassOfDictionary(dictionary)