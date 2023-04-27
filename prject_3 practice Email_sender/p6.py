import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content

os.environ['SENDGRID_API_KEY'] = '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'


def send_email(content, emails):
    from_email = Email("ziamalhi1234@gmail.com")
    to_emails = To(emails.split(','))

    subject = "Email from SendGrid and Python"
    plain_text_content = Content("text/plain", content)

    message = Mail(
        from_email=from_email,
        to_emails=to_emails,
        subject=subject,
        plain_text_content=plain_text_content
    )

    try:
        sg = SendGridAPIClient()
        response = sg.send(message)

        print(response.status_code)
        print(response.body)
        print(response.headers)

    except Exception as e:
        print(e.message)


content = input("Enter your email content: ")
emails = input("Enter the email addresses separated by commas: ")

send_email(content, emails)
