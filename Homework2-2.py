#1 по адресу http://127.0.0.1//requirements - вывести на странице содержимое файла requirements.txt
#2 Вывести 100 случайно сгенерированных юзеров на локалхост (почта + имя) 'Dmytro aasdasda@mail.com' PATH: /generate-users/ ( https://pypi.org/project/Faker/ ) + параметр который регулирует количество юзеров
#3 Вывести количество космонавтов в настоящий момент (http://api.open-notify.org/astros.json) (https://pypi.org/project/requests/) PATH: /space/
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) 
def text():

    from  faker  import  Faker     
    fake  =  Faker ( ['it_IT', 'ru_RU', 'uk_UA'] ) 
    for  c  in  range ( 99 ):
        my_file = open("mails.txt", 'a') 
        c = fake.free_email()
        my_file.write(c + '\n')
        my_file.close()
        
           #На странице выводило по одному мылу,за одно обновление страницы
           #поэтому, решил записать файл и выгрузить с него на страницу 
           #но слешн не отработал как ожидалось 
           #в общем, собирал код из говна и палок, жду комментариев
    
    with open('mails.txt') as mail:
        return mail.read()
   
   

if __name__ == "__main__":
    app.run(debug=True) #For reload server after changed code