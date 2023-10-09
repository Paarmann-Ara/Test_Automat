from jtl_wawi.testcase.sample_dictionary.testcase_sample_dictionary import TestcaseSampleDictionary

#--
#...
#-- 

class TestcaseSampelProvider:
    def __init__(self, sample_file) -> None:
        #get testcase object config from fconfig.json
        self.testcase_sample_config_dictionary = TestcaseSampleDictionary().instance.dictionary
        testcase_sample_file_dictionary = self.testcase_sample_config_dictionary['testcase_sample_file_dictionary']
                

        sample_file_dictionary = TestcaseSampleDictionary(dictionary_fulladress=testcase_sample_file_dictionary).instance.dictionary

        self.full_adress = sample_file_dictionary[sample_file]
        file_list = self.full_adress.split('/')
        self.file = file_list[-1]
        self.directory = '/'.join(file_list[:-1])
        
         