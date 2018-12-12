from flask import render_template
from flask_mail import Message
from app import app, mail
from threading import Thread

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, body_text, body_html):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = body_text
    msg.html = body_html
    Thread(target=send_async_email, args=(app, msg)).start()

def send_password_reset_email(user):
    token = user.get_reset_password_token() # default expires after 600 secs
    send_email('[Microblog] Password Reset',
        sender=app.config['ADMINS'][0],
        recipients=[user.email],
        body_text=render_template('email/reset_password.txt', user=user, token=token),
        body_html=render_template('email/reset_password.html', user=user, token=token))


