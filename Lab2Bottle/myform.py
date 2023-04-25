from bottle import post, request,view,template,datetime
import re
import pdb
import json
import os
import myform_mail
from datetime import date

@post('/myform',method='post')
@view('myform')

def my_form():
    #получение значений полей с формы
    mail = request.forms.get('ADRESS')
    name = request.forms.get('NAME')
    question = request.forms.get('QUEST')
    current_date = date.today()
    
    #проверка на пустоту поля вопроса
    if(question == "" or question == " "):
        return template('index.tpl',year=datetime.now().year,error="Fill in field Your Question",quest=question,name=name,email=mail)
    #проверка на количество символов в вопросе
    elif(len(question)<=3):
        return template('index.tpl',year=datetime.now().year,error="Your Question must be more than 3 symbols",quest=question,name=name,email=mail)
    #проверка на то,что в вопросе содержаться только числа
    elif(question.isdigit()):
        return template('index.tpl',year=datetime.now().year,error="Your Question have to contains not only digits!",quest=question,name=name,email=mail)
    #проверка на пустоту поля имени
    elif (name == "" or name == " "):
        return template('index.tpl',year=datetime.now().year,error="Fill in field Your Name",quest=question,name=name,email=mail)
    #проверка на пустоту поля почты
    elif(mail == "" or mail == " "):
        return template('index.tpl',year=datetime.now().year,error="Fill in field Your Email",quest=question,name=name,email=mail)
    #проверка на соответствие почты регулярному выражению
    elif not myform_mail.mail_match(mail):
        return template('index.tpl',year=datetime.now().year,error="Email isn't match the format",quest=question,name=name,email=mail) 
    else:
        questions={}
        #проверка на существование файла
        if os.path.exists('user_questions.json'):
            #открытие файла
            with open('user_questions.json', 'r') as read_json:
                #проверка на пустоту файла
                if (os.path.getsize('user_questions.json') > 0):
                    #чтение из файла
                    questions = json.load(read_json)
        #открытие на запись(если файла нет, он создается)
        with open('user_questions.json', 'w') as write_json:
            #если почта уже есть в считанном словаре, то происходит проверка был ли задан такой вопрос,если был,
            # то добавление не происходит,если не был,то вопрос добавляется в словарь
            if mail in questions:
                #цикл по именам во вложенном словаре 
                for i in questions.get(mail):
                    #проверка на наличие имени в словаре
                    if name in i:
                        #проверка на наличие вопроса по имени
                        if question.lower() not in i.get(name):
                            i.get(name).append(question.lower())
                        else:
                            json.dump(questions, write_json)
                            #вывод сообщения о том,что такой вопрос уже был задан
                            return template('index.tpl',year=datetime.now().year,error="Sorry {0},this question is exist".format(name),quest=question,name=name,email=mail)
                    else:
                        i[name]=[question.lower()]
            else:
        #если такого пользователя еще нет в словаре то в словарь добавляется его email,username и вопрос
                questions[mail]=[{name:[question.lower()]}]
            #запись в json
            json.dump(questions, write_json)
        #обратная связь об успешности доступа
        return dict(message="Thanks, {0} !The answer will be sent to the mail {1}. Access date: {2} ".format(name,mail,current_date))
        