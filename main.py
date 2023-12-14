import boto3
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
import logging

class SendEmail:
    def __init__(self, registered_sender, issued_to, moded_subject, attach_pdf, attach_xml, region_name):
        """
        Initialize the SendEmail instance.

        Parameters:
        - registered_sender (str): The email address of the sender.
        - issued_to (str): The email address of the recipient.
        - moded_subject (str): The subject of the email.
        - attach_pdf (str): Path to the PDF file to attach.
        - attach_xml (str): Path to the XML file to attach.
        - region_name (str): The AWS region for SES.
        """
        self.registered_sender = registered_sender
        self.issued_to = issued_to
        self.moded_subject = moded_subject
        self.attach_pdf = attach_pdf
        self.attach_xml = attach_xml
        self.region_name = region_name
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def send_email(self):
        """
        Send an email with attachments using Amazon SES.
        """
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

        for file_path, content_type in [(self.attach_pdf, 'application/pdf'), (self.attach_xml, 'application/xml')]:
            with open(file_path, 'rb') as file:
                attachment = MIMEApplication(file.read(), _subtype=os.path.splitext(file_path)[1][1:])
                attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_path))
                message.attach(attachment)

        try:
            response = ses.send_raw_email(
                Source=message['From'],
                Destinations=[message['To']],
                RawMessage={'Data': message.as_string()}
            )
            self.logger.info(f"Email sent successfully. MessageId: {response['MessageId']}")
        except ClientError as e:
            self.logger.error(f"Error sending email: {e}")

if __name__ == "__main__":
    sender = 'your_sender@example.com'
    recipient = 'recipient@example.com'
    subject = 'Your Subject'
    pdf_path = 'path/to/your/file.pdf'
    xml_path = 'path/to/your/file.xml'
    aws_region = 'your_aws_region'

    email_sender = SendEmail(sender, recipient, subject, pdf_path, xml_path, aws_region)
    email_sender.send_email()
