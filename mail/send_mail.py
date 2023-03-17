from log_all import log_me
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import smtplib
import os
from typing import Any

# --
# ...
# --


class SendMail():
    pass

    @staticmethod
    def send_mail(html_body={'html':'', 'body':''}, from_addr='', to_addr='', cc_addr_list='', subject='', login='', password='', smtpserver='', attach ={'attach_item' : {'is_attach' : True, 'is_all_directory' : False, 'directory' : '', 'file' :''}}) -> bool:
        
        log_me.INFO(__name__)
        
        try:

            to_addr = to_addr.split(",")

            message = MIMEMultipart('alternative')
            message['subject'] = subject
            message['From'] = from_addr
            message['Cc'] = cc_addr_list

            body = MIMEText(html_body['body'], 'plain')
            html = MIMEText(html_body['html'], 'html')

            message.attach(body)
            message.attach(html)
            
            for attached_file in SendMail.attach(attach) : message.attach(attached_file)

            server = smtplib.SMTP(smtpserver)
            server.starttls()
            server.login(login, password)

            for to_addr_list in to_addr:
                message['To'] = to_addr_list
                server.sendmail(from_addr, to_addr_list, message.as_string())
                
            server.quit()
            
            return True

        except Exception as exp:
            log_me.ERROR(__name__ + str(exp))
            return False

# --
# ...
# --

    @staticmethod
    def attach(attach ={'attach_item' : {'is_attach' : True, 'is_all_directory' : False, 'directory' : '', 'file' :''}}) -> Any:
        
        log_me.INFO(__name__)
        
        try:
            
            files = []
            attachments = []
            
            for item in attach:
                item = attach[item]
                is_attach = item['is_attach']
                is_all_directory = item['is_all_directory']
                directory = item['directory']
            
                if is_attach:
                    if bool(os.listdir(directory)):
                        
                        if is_all_directory:
                            for Item in os.listdir(directory): files.append(directory + '#' + item['file'])
                        else:
                            files.append(directory + '#' + item['file'])
                            
            attachments = SendMail.create_holder(files)

            return attachments
                    
        except Exception as exp:
            log_me.ERROR(__name__ + str(exp))
            
# --
# ...
# --

    @staticmethod
    def create_holder(files):
        
        log_me.INFO(__name__)
        
        try:
            
            temp_attachments = []
            files = set(files)
            #f = list(dict.fromkeys(File))
            _ = 0
                
            for item in files:
                item = item.split('#')
                attachment = open(item[0] + item[1], "rb")
                
                temp_attachments.append(MIMEBase('application', 'octet-stream'))
                temp_attachments[_].set_payload((attachment).read())
                encoders.encode_base64(temp_attachments[_])
                
                temp_attachments[_].add_header(
                    'Content-Disposition', "attachment; filename= %s" % item[1])
                
                _ += 1
                
            return temp_attachments
        
        except Exception as exp:
            log_me.ERROR(__name__ + str(exp))