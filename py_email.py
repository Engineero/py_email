#*******************************************************************************
# Filename: py_email.py
# Language: Python
# Author: engineero
# Created: 2020-08-31
#*******************************************************************************
"""Script for sending emails from Python.

Can also be used to send a text message using the appropriate carrier's
domain."""


from argparse import ArgumentParser
from smtplib import SMTP
from email.message import EmailMessage


def check_args(args):
    """Checks arguments, throws errors if there are problems."""

    pass


def send_message(msg, server):
    """Sends an email using an SMTP server."""

    with SMTP(server) as s:
        s.send_message(msg)


def main(args):

    """Compiles and sends the email message."""
    msg = EmailMessage()
    msg.set_content(args.message)
    msg['Subject'] = args.subject
    msg['From'] = args.from_addr
    msg['To'] = args.to_addr
    send_message(msg, args.server)
    print('Message sent!')


if __name__ == '__main__':
    parser = ArgumentParser(description='Sends emails from Python.')

    parser.add_argument('to_addr', type=str,
                        help='Destination email address.')
    parser.add_argument('from_addr', type=str,
                        help="Sender's email address.")
    parser.add_argument('message', type=str,
                        help='Email message content.')
    parser.add_argument('--subject', type=str, default='Hi!',
                        help='Email message subject. Default is "Hi!"')
    parser.add_argument('--server', type=str, default='localhost',
                        help='SMTP server address. Default is "localhost".')

    args = parser.parse_args()
    check_args(args)
    main(args)


#*******************************************************************************
#                                END OF FILE
#*******************************************************************************
