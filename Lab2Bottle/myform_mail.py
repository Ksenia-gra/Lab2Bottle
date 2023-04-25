import re
def mail_match(mail):
    regex = re.compile(r'([A-Za-z0-9]+[._-])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})$')
    match = re.match(regex, mail)
    return bool(match)