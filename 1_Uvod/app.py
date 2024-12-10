from datetime import datetime
import pytz # pip install pytz
# pytz umoznuje presne a medzikrokova vypocty casovych pasiem
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    nyc_timezone = pytz.timezone('America/New_York')
    html = []
    html.append("<h1>Hello New York!</h1>")
    html.append("<p>Odstavec</p>")
    html.append(f"<h2>Aktualni cas v SR: {datetime.now().strftime('%H: %M')}</h2>")
    html.append(f"<h2>Mistni cas v NY: {datetime.now(nyc_timezone).strftime('%H: %M')}</h2>")

    return "".join(html)

# Terminal: FLASK_APP=app.py flask run