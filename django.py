#code to be write in views.py

import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email=os.environ.get('FROM_EMAIL'),
    to_emails=os.environ.get('TO_EMAIL'),
    subject='Mail Testing',
    html_content='<strong>HTML file here</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
    print('success')
except Exception as e:
    print(e)
    
#code to be write in settings.py

from dotenv import load_dotenv
import os
load_dotenv()



EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('FROM_EMAIL')
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_API_KEY')

#make an .env file to store your email and its password.
