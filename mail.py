import smtplib
# from email.MIMEMultipart import MIMEMultipart
# from email.MIMEText import MIMEText
# from email.MIMEImage import MIMEImage

# Email you want to send the update from (only works with gmail)
fromEmail = 'iisc.invaliddatatypes@gmail.com'
# You can generate an app password here to avoid storing your password in plain text
# https://support.google.com/accounts/answer/185833?hl=en
fromEmailPassword = 'saghdlnmponpbwvg'

# Email you want to send the update to
toEmail = 'vishwanath.21bce7893@vitapstudent.ac.in'

def sendEmail():
	# msgRoot = MIMEMultipart('related')
	# msgRoot['Subject'] = 'Security Update'
	# msgRoot['From'] = fromEmail
	# msgRoot['To'] = toEmail
	# msgRoot.preamble = 'Raspberry pi security camera update'

	# msgAlternative = MIMEMultipart('alternative')
	# msgRoot.attach(msgAlternative)
	# msgText = MIMEText('Smart security cam found object')
	# msgAlternative.attach(msgText)

	# msgText = MIMEText('<img src="cid:image1">', 'html')
	# msgAlternative.attach(msgText)

	# msgImage = MIMEImage(image)
	# msgImage.add_header('Content-ID', '<image1>')
	# msgRoot.attach(msgImage)
	subject = 'Chetan test subject'
	body = 'Hello Hello Hello'
	msg = f'Subject: {subject}\n\n{body}'

	smtp = smtplib.SMTP('smtp.gmail.com', 587)
	smtp.starttls()
	smtp.login(fromEmail, fromEmailPassword)
	smtp.sendmail(fromEmail, toEmail, msg)
    
	smtp.quit()

sendEmail()
