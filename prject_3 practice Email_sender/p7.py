import sendgrid

sg = sendgrid.SendGridAPIClient(api_key='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')
data = {
  "personalizations": [
    {
      "to": [
        {
          "email": "ziamalhi786@gmail.com",
        }
      ],
      "subject": "Hello World from the SendGrid Python Library!"
    }
  ],
  "from": {
    "email": "ziamlhi1234@gmail.com"
  },
  "content": [
    {
      "type": "text/plain",
      "value": "Hello, Email!"
    }
  ]
}
response = sg.client.mail.send.post(request_body=data)
print(response.status_code)
