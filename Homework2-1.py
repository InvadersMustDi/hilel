#1 по адресу http://127.0.0.1//requirements - вывести на странице содержимое файла requirements.txt
#2 Вывести 100 случайно сгенерированных юзеров на локалхост (почта + имя) 'Dmytro aasdasda@mail.com' PATH: /generate-users/ ( https://pypi.org/project/Faker/ ) + параметр который регулирует количество юзеров
#3 Вывести количество космонавтов в настоящий момент (http://api.open-notify.org/astros.json) (https://pypi.org/project/requests/) PATH: /space/
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET']) #method to get files only
def text():
    with open('requirements/requirements.txt') as req:
        return req.read() #read from file
   

if __name__ == "__main__":
    app.run(debug=True) #For reload server after changed code