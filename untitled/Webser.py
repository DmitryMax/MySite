import random
from flask import Flask, render_template

app = Flask(__name__)
weat = [
    {'name': 'солнечная погода', 'imge': '10042.jpg'},
    {'name': 'дождливая погода', 'imge': 'rain.jpg'},
    {'name': 'град', 'imge': 'grad.jpg'}
        ]

@app.route('/main menu')
def about():
    return  render_template('main_menu.html')

@app.route('/me')
def me():
    return render_template('Pavel1.html')

@app.route('/weather')
def weather():
    day_weat = random.choice(weat)
    return render_template('weather.html', w = day_weat)


app.run(debug=True, port=8080)