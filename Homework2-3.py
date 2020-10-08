from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) 
def space():
    import requests
    r = requests.get('http://api.open-notify.org/astros.json')
    cosmonauts = r.json()
    #print (cosmonauts)
    return cosmonauts

if __name__ == "__main__":
    app.run(debug=True) #For reload server after changed code