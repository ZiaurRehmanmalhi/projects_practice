import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


message = Mail(from_email='ziamalhi1234@gmail.com',
               to_emails='mujeeburr661@gmail.com',
               subject='demo',
               plain_text_content='even with python.',
               html_content='<strong>and easy to do anywhere, even with python</strong>')
try:
    sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
