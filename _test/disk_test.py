from disk.json.json_manager import JSONManager
from disk.xml.xml_manager import XMLManager
from toolboxs.toolbox import Toolbox
import pprint

ROOT_DIR = Toolbox.get_root_path()

json = JSONManager().instance
json_dicttionary = json.operation(ROOT_DIR + r'\config.json')

# --
# ...
# --

json_dicttionary = """{
        "db_dictionary":{
            "Driver": "SQL Server",
            "Host": "LocalHost\\JTLWAWI",
            "Database": "master",
            "UserName": "sa",
            "Password" : "sa04jT14"
        }
    }"""
    
json.operation(ROOT_DIR + f"\config.json", json_dicttionary)

# --
# ...
# --

xml = XMLManager().instance
xml_dicttionary = xml.operation(ROOT_DIR + r'\xml_test.xml', is_get_dictionary = True)
pprint.pprint(xml_dicttionary, indent=2)

# --
# ...
# --

xml_dicttionary = xml.operation(ROOT_DIR + r'\xml_test_0.xml', xml_dicttionary)