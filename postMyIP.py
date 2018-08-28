#!/usr/bin/env python3

import socket
import smtplib
import os
import sys

from email.mime.text import MIMEText
from socket import gethostname
from pathlib import Path

SMTP_IP = '1.1.1.1'
TO_EMAIL = 'email@email.com'
FROM_EMAIL = 'email@email.com'
DIR_NAME = "/root/"


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        print(s.getsockname()[0])
        print(gethostname())
        my_file = Path(DIR_NAME + str(s.getsockname()[0]) + '.myip')
        if my_file.is_file():
                print(s.getsockname()[0] + ' exists. Exiting.')
                sys.exit()
        else:
                test = os.listdir(DIR_NAME)
                for item in test:
                        if item.endswith(".myip"):
                                os.remove(os.path.join(DIR_NAME, item))
                with open(DIR_NAME + s.getsockname()[0]  + '.myip', 'w') as f:
                        f.write("")
                print(s.getsockname()[0] + ' created.')
                msgtxt  = str(gethostname()) + '\'s IP#: ' + str(s.getsockname()[0]) + '\n'
                msg = MIMEText(msgtxt)
                msg['Subject'] = '[' + str(gethostname()) + '] My IP#: ' + str(s.getsockname()[0])
                msg['From'] = TO_EMAIL
                msg['To'] = FROM_EMAIL
                mail = smtplib.SMTP(SMTP_IP)
                print('Posting notification Email')
                mail.send_message(msg)
                mail.quit()
