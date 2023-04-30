import sendgrid
from sendgrid.helpers.mail import Mail

try:
    sg = sendgrid.SendGridAPIClient(api_key='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')
    message = Mail(
        from_email='ziamalhi1234@gmail.com',
        to_emails='ziamalhi786@gmail.com',
        subject='Sending with SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
