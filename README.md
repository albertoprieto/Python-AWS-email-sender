# Python AWS Email Sender

This Python script utilizes Amazon Simple Email Service (SES) to send emails with attachments.

## Requirements

- Python 3.x
- Python libraries (install with `pip install -r requirements.txt`):
- boto3

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/albertoprieto/Python-AWS-email-sender.git
   cd Python-AWS-email-sender
   ```
2. Create a virtual environment (optional but recommended):

  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```
3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
4. Configure environment variables:

  Create a .env file with the following variables:
  ```bash
  AWS_ACCESS_KEY_ID=your_access_key_id
  AWS_SECRET_ACCESS_KEY=your_secret_access_key
  ```
Make sure to include this file in your .gitignore to avoid sharing your credentials on Git.

Usage
Run the script by providing the following environment variables:

  SENDER_EMAIL: Sender's email address.
  RECIPIENT_EMAIL: Recipient's email address.
  EMAIL_SUBJECT: Email subject.
  PDF_PATH: Path to the PDF file to attach.
  XML_PATH: Path to the XML file to attach.
  AWS_REGION: AWS region for SES.

Example:
  ```bash
  export SENDER_EMAIL=your_sender@example.com
  export RECIPIENT_EMAIL=recipient@example.com
  export EMAIL_SUBJECT='Your Subject'
  export PDF_PATH='path/to/your/file.pdf'
  export XML_PATH='path/to/your/file.xml'
  export AWS_REGION='your_aws_region'

  python main.py
  ```
