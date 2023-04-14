from bottle import post, request,view,template,datetime
import re
import pdb
import json
import os
from datetime import date

@post('/myform',method='post')
@view('myform')
def my_form():
    mail = request.forms.get('ADRESS')
    name = request.forms.get('NAME')
    question = request.forms.get('QUEST')
    current_date = date.today()
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    match = re.match(regex, mail)
    if(question == "" or question == " "):
        return template('index.tpl',year=datetime.now().year,error="Fill in field Your Question",quest=question,name=name,email=mail)
    elif(len(question)<=3):
        return template('index.tpl',year=datetime.now().year,error="Your Question must be more than 3 symbols",quest=question,name=name,email=mail)
    elif(question.isdigit()):
        return template('index.tpl',year=datetime.now().year,error="Your Question have to contains not only digits!",quest=question,name=name,email=mail)
    elif (name == "" or name == " "):
        return template('index.tpl',year=datetime.now().year,error="Fill in field Your Name",quest=question,name=name,email=mail)
    elif(mail == "" or mail == " "):
        return template('index.tpl',year=datetime.now().year,error="Fill in field Your Email",quest=question,name=name,email=mail)
    elif not match:
        return template('index.tpl',year=datetime.now().year,error="Email isn't match the format",quest=question,name=name,email=mail) 
    else:
        questions={}
        if os.path.exists('user_questions.json'):
            with open('user_questions.json', 'r') as read_json:
                if (os.path.getsize('user_questions.json') > 0):
                    questions = json.load(read_json)
            with open('user_questions.json', 'w') as write_json:
                if mail in questions:
                    if question.lower() not in questions.get(mail):
                        questions.get(mail).append(question.lower())
                else:
                    questions[mail]=[name]
                    questions.get(mail).append(question.lower())
                json.dump(questions, write_json)
        return dict(message="Thanks, {0} !The answer will be sent to the mail {1}. Access date: {2} ".format(name,mail,current_date))
        