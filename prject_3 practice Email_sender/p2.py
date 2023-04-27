import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email(from_email, to_email, subject, plain_text_content, html_content):
    message = Mail(from_email=from_email,
                   to_emails=to_email,
                   subject=subject,
                   plain_text_content=plain_text_content,
                   html_content=html_content)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(f'Status code: {response.status_code}')
        print(f'Response body: {response.body}')
        print(f'Response headers: {response.headers}')
    except Exception as e:
        print(str(e))


send_email('zaimalhi1234@gmail.com',
           'mujeeburr661@gmail.com',
           'Subject line',
           'Plain text message',
           '<strong>HTML message</strong>')
