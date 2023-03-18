from services.mail.base_mail_template import BaseMailTemplate


# --
# ...
# --

class TestCompleteResultTemplate(BaseMailTemplate):
        
    @classmethod
    def get_template(cls, body: str)-> str:
            
        html = """
                <html>
                    <head>
                        <style>
                            div.content { width: 15000px }
                            h1 {color:red;font-family: Arial;font-size: 80%;font-weight:lighter;}
                            h2 {color:green;font-family: Arial;font-size: 80%;}
                            h3 {color:black;font-family: Arial;font-size: 80%;font-weight:lighter;}
                            p {color:blue;font-family: Lucida Console;font-size: 80%;}
                        </style>
                    </head>
                      
                    <body>
                        <div class="content">
                        """ + f"{body}" + """
                        </div>
                    </body>
                </html>
            """
                
        return html