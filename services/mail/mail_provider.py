from services.mail.core.mail import Mail
from services.log_.log_provider import LogProvider


class MailProvider:
    def __init__(self, template='TestCompleteResult', body='',subject='', attach_object=None, domain='jtl', sender='tc', recipient={'recipient_address':['mohammad.paarmann-ara'], 'recipient_cc': ['mohammad.paarmann-ara']}) -> None:
        self.log_info_class = LogProvider().info
        self.log_error_class = LogProvider().error
        
        self.tc_mo_instance = Mail(template=template, body=body, subject=subject, attach_object=attach_object, domain=domain, sender=sender, recipient=recipient, log_info_class=self.log_info_class, log_error_class=self.log_error_class).instance
