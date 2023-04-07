from bottle import post, request,view
import re
from datetime import date

@post('/myform',method='post')
@view('myform')
def my_form():
    mail = request.forms.get('ADRESS')
    name = request.forms.get('NAME')
    current_date = date.today()
    regex=re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    res=""
    match = re.match(regex, mail)
    if match:
        res="Thanks, {0} !The answer will be sent to the mail {1}. Access date: {2} ".format(name,mail,current_date)
    else:
        res="Sorry, {0}, email isn't match the format,get back and try again.Access date: {1}".format(name,current_date)
    return dict(message=res)

