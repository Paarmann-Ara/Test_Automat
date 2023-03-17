from mail.templates.testcomplete_result import TestCompleteResultTemplate
from mail.send_mail import SendMail
from mail.config.mail_config import EmailConfig
from wawi.config.test_case.test_case_config import TestCaseConfig

html_body = TestCompleteResultTemplate(body='BODY Ke Sakhtam')()

mail_config = EmailConfig().instance
from_addr = mail_config('TC_Address')
to_addr = mail_config('Default_Sender_Address')
cc_addr_list = mail_config('Default_Dev_Address')
subject = 'TestNeuePlatform'
login = mail_config('TC_Address')
password = mail_config('TC_Password')
smtpserver= mail_config('TC_MailServer_SMTP')

test_case_dictionary = TestCaseConfig().instance

# attachments = {
#                 'AttachItem_0' : {
#                         'is_attach' : True, 
#                         'is_all_directory' : True,
#                         'directory' : test_case_dictionary('Recorder_Address'), 
#                         'file' : test_case_dictionary('Recorder_FileName')
#                         },
                
#                 'AttachItem_1' : {
#                         'is_attach' : True, 
#                         'is_all_directory' : True,
#                         'directory' : test_case_dictionary('Recorder_Address'), 
#                         'file' : test_case_dictionary('Recorder_FileName_0')
#                         },
#           }

# SendMail.send_mail(html_body, from_addr, to_addr, cc_addr_list, subject, login, password, smtpserver, attachments)

# --
# ...
# --

attachments = {
                'AttachItem_0' : {
                        'is_attach' : True, 
                        'is_all_directory' : False,
                        'directory' : test_case_dictionary('Recorder_Address'), 
                        'file' : test_case_dictionary('Recorder_FileName')
                        },
                
                'AttachItem_1' : {
                        'is_attach' : True, 
                        'is_all_directory' : False,
                        'directory' : test_case_dictionary('Recorder_Address'), 
                        'file' : test_case_dictionary('Recorder_FileName_0')
                        },
          }

SendMail.send_mail(html_body, from_addr, to_addr, cc_addr_list, subject, login, password, smtpserver, attachments)