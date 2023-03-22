from wawi.testcase.testcase_object_provider import TestCaseObjectProvider
from drivers.test_complete.test_complete_driver import TestCompleteDriver


#--
#...
#--


class TestCompleteWawiHandler():
    def __init__(self) -> None:
        self.objects_context_menu = TestCaseObjectProvider('objects_context_menu').object_dictionary
        self.test_complete_driver = TestCompleteDriver(self.objects_context_menu).instance


TestCompleteWawiHandler().test_complete_driver.wait_for_availability('kjhbgigh       9')
