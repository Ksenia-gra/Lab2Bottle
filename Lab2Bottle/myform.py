from bottle import post, request,view,template,datetime
import re
import pdb
import json
from os.path import exists
from datetime import date

@post('/myform',method='post')
@view('myform')
def my_form():
    mail = request.forms.get('ADRESS')
    name = request.forms.get('NAME')
    question = request.forms.get('QUEST')
    current_date = date.today()
    regex=re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    match = re.match(regex, mail)
    if(question=="" or question==" "):
        return template('index.tpl',year=datetime.now().year,error="Fill in field Your Question",quest=question,name=name,email=mail)
    elif (name=="" or name==" "):
        return template('index.tpl',year=datetime.now().year,error="Fill in field Your Name",quest=question,name=name,email=mail)
    elif(mail=="" or mail==" "):
        return template('index.tpl',year=datetime.now().year,error="Fill in field Your Email",quest=question,name=name,email=mail)
    elif not match:
        return template('index.tpl',year=datetime.now().year,error="Email isn't match the format",quest=question,name=name,email=mail) 
    else:
        questions={}
        if mail in questions:
            questions.get(mail).append(question)
        else:
            questions={mail:[name]}
            questions.get(mail).append(question)
        pdb.set_trace()
        return dict(message="Thanks, {0} !The answer will be sent to the mail {1}. Access date: {2} ".format(name,mail,current_date))
        