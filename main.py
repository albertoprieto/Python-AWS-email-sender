import boto3
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

class SendEmail():
    def __init__(self):
        self.registered_sender = ''
        self.issued_to = ''
        self.moded_subject = ''
        self.attach_pdf = ''
        self.attach_xml = ''
        self.region_name = ''
        
    def main(self):
        ses = boto3.client('ses', region_name=self.region_name)
        message = MIMEMultipart()
        message['Subject'] = f'{self.moded_subject}'
        message['From'] = self.registered_sender
        message['To'] = self.issued_to

        body_message = f"""
        <img src="your_path" alt="Your logo" width="350" height="130">
        <p>Body:</p>
        <ol>
            <li><strong>Attachment XML:</strong> {os.path.basename(self.attach_xml)}</li>
            <li><strong>Attachment PDF:</strong> {os.path.basename(self.attach_pdf)}</li>
        </ol>

        """

        message.attach(MIMEText(body_message, 'html'))

        with open(self.attach_pdf, 'rb') as pdf_file:
            att_pdf = MIMEApplication(pdf_file.read())
            att_pdf.add_header('Content-Disposition', 'attachment', filename=os.path.basename(self.attach_pdf))
            message.attach(att_pdf)

        with open(self.attach_xml, 'rb') as xml_file:
            att_xml = MIMEApplication(xml_file.read())
            att_xml.add_header('Content-Disposition', 'attachment', filename=os.path.basename(self.attach_xml))
            message.attach(att_xml)

        try:
            response = ses.send_raw_email(
                Source=message['From'],
                Destinations=[message['To']],
                RawMessage={'Data': message.as_string()}
            )
            print(response['MessageId'],response)
        except ClientError as e:
            print(e)
