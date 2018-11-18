import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient('SG.gwR2h6-MRJ6M-tL2JP0M6Q.f813z-OsNhKycS6wpzKYG5pJcPY0FgJxs0kpKRSOzWQ')
from_email = Email("test@example.com")
to_email = Email("matthew.guptil@duke.edu")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)