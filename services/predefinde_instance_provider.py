from services.mail.mail_provider import MailProvider
from wawi.testcase.testcase_sample_provider import TestcaseSampelProvider
from wawi.testcase.testcase_object_provider import TestcaseObjectProvider

class PredefindeInstance:
    def __init__(self) -> None:
        tc_mo = MailProvider(body='Test_body', subject='Test_Subjekt').tc_mo_instance
        
        objects_context_menu = TestcaseObjectProvider('objects_context_menu').object_class
        Simple_CSV_AnhangDatei = TestcaseSampelProvider('Simple_CSV_AnhangDatei').full_adress    