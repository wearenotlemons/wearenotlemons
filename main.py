from flask import Flask, request, render_template, redirect, url_for
import requests
from urllib.parse import quote

SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbysuJ_-IhAHQC6cU7s2o2zcNOF3pEs72D_ryKbG21fs0KhwPvkgjQjf9GEjlPtkatrG/exec'

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    name = request.args.get('name')
    msg = request.args.get('msg')
    sessions = request.args.get('sessions')
    totalHours = request.args.get('totalHours')

    return render_template(
        'index.html',
        name=name,
        msg=msg,
        sessions=sessions,
        totalHours=totalHours
    )

@app.route('/', methods=['POST'])
def submit():
    name = request.form.get('nameInput')
    if not name:
        return redirect(url_for('index', msg="Please enter a name."))

    data_dict = get_data(name)
    if data_dict:
        name = data_dict.get('name')
        sessions = ", ".join(map(str, data_dict.get('sessions', [])))
        totalHours = data_dict.get('totalHours')
        if totalHours > 0:
            return redirect(url_for('index', name=name, sessions=sessions, totalHours=totalHours))
        else:
            return redirect(url_for('index', name=name, msg="You did not attend any sessions."))
    else:
        return redirect(url_for('index', msg="Failed to retrieve data. Please try again."))

def get_data(name) -> dict:
    encoded_name = quote(name)
    try:
        print(f"Request URL: {SCRIPT_URL}?name={encoded_name}")
        response = requests.get(f"{SCRIPT_URL}?name={encoded_name}")
        response.raise_for_status()  # Will raise an exception for 4xx/5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print("❌ Request failed:", e)
        return None
    except ValueError as ve:
        print("❌ Error decoding JSON:", ve)
        return None

app.run()
