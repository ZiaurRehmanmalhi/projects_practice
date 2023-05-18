import os
import sendgrid
from sendgrid.helpers.mail import Content, Email, Mail

# Set the SendGrid API key
os.environ['SENDGRID_API_KEY'] = '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'

# Create the SendGrid client
sg = sendgrid.SendGridAPIClient(api_key=os.environ['SENDGRID_API_KEY'])

# Compose the email
from_email = Email("ziamalhi1234@gmail.com")
to_email = Email("ziamalhi786@gmail.com")
subject = "A test email from Sendgrid"
content = Content(
    "text/plain", "Here's a test email sent through Python"
)
mail = Mail(from_email, subject, to_email, content)

# Send the email
try:
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(str(e))
