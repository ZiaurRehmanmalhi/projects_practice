import sendgrid
import os
from sendgrid.helpers.mail import *


class Content:
    def __init__(self, content):
        self.content = content


api_key = "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"
sg = sendgrid.SendGridAPIClient({api_key})
from_email = Email("ziamalhi1234@gmail.com")
to_email = Email("ziamalhi15@gmail.com")
subject = "Sending with sendgrid"
content = Content("send wit python")
mail = Mail(from_email, subject, to_email, content)


response = sg.client.maiil.send.post(request_body=mail.get())


print(response.status_code)
print(response.body)
print(response.headers)
