import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
speaking_engine = pyttsx3.init()

def talk(text):
    speaking_engine.say(text)
    speaking_engine.runAndWait()

def get_information():
    try:
        with sr.Microphone() as source:
            print("listening..")
            voice = listener.listen(source)
            information = listener.recognize_google(voice)
            print(information)
            return information.lower()
    except:
        pass


def send_email(receiver, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('sender_email','sender_password')
    email = EmailMessage()
    email['From']='sender_email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)

email_list =  {
    'programmer': 'receiver_email'
}


def get_email_information():
    talk('Who is the receiver of this mail?')
    name = get_information()
    receiver = email_list[name]
    print(receiver)
    print("The receiver is:" + receiver)
    talk("Tell us the subject")
    subject = get_information()
    talk('What is the content')
    content = get_information()

    send_email(receiver, subject, content)
    talk('Hey, the email is sent')
    talk("Do you want to send more? Say YES or No")
    send_more = get_information()
    if 'yes' in send_more:
        get_email_information()

get_email_information()
