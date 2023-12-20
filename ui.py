from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from main import SendEmail


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) / 255.0 for i in (0, 2, 4))
    

class EmailApp(App):

    def build(self):
        self.ui = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.ui.background_color = hex_to_rgb('#4287f5')
        text_color = hex_to_rgb('#FFFFFF')
        
        self.sender_email = TextInput(hint_text='Sender Email', foreground_color=text_color)
        self.recipient_email = TextInput(hint_text='Recipient Email', foreground_color=text_color)
        self.email_subject = TextInput(hint_text='Subject', foreground_color=text_color)
        self.pdf_file_chooser = FileChooserIconView(path='/path/to/default/pdf/folder')
        self.xml_file_chooser = FileChooserIconView(path='/path/to/default/xml/folder')
        self.send_button = Button(text='Send Email', on_press=self.send_email, background_color=(0.4, 0.8, 0.4, 1))
        self.status_label = Label(color=text_color)

        self.ui.add_widget(self.sender_email)
        self.ui.add_widget(self.recipient_email)
        self.ui.add_widget(self.email_subject)
        self.ui.add_widget(Label(text='PDF Attachment', color=text_color))
        self.ui.add_widget(self.pdf_file_chooser)
        self.ui.add_widget(Label(text='XML Attachment', color=text_color))
        self.ui.add_widget(self.xml_file_chooser)
        self.ui.add_widget(self.send_button)
        self.ui.add_widget(self.status_label)

        return self.ui

    def send_email(self, instance=None):
        sender_email = self.sender_email.text
        recipient_email = self.recipient_email.text
        email_subject = self.email_subject.text
        pdf_path = self.pdf_file_chooser.path
        xml_path = self.xml_file_chooser.path

        if not sender_email or not recipient_email or not email_subject or not pdf_path or not xml_path:
            self.status_label.text = 'Please fill in all fields.'
            return

        try:
            send_email_instance = SendEmail(
                registered_sender=sender_email,
                issued_to=recipient_email,
                moded_subject=email_subject,
                attach_pdf=pdf_path,
                attach_xml=xml_path,
                region_name='us-west-2'
            )
            self.status_label.text = 'Email sent successfully.'
        except Exception as e:
            self.status_label.text = f'Error sending email: {str(e)}'


if __name__ == '__main__':
    EmailApp().run()
