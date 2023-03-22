from services.mail.templates.testcomplete_result import TestCompleteResultTemplate

#--
#...
#--


class MailTemplateDictionary():

    def __call__(self) -> dict:
        self.dictionary = {
            "TestCompleteResult": TestCompleteResultTemplate,
        }

        return self.dictionary