import requests
from flask import Blueprint, render_template, request, flash, redirect, url_for

main = Blueprint('main', __name__)

TELEGRAM_TOKEN = '8153302891:AAGkMF6c5_sBfnu3UdTGeq7Wtph5NWGALsE'
TELEGRAM_CHAT_ID = '927533634'

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    text = f"📩 Nowa wiadomość z CV!\n\nImię: {name}\nEmail: {email}\nWiadomość:\n{message}"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
    try:
        requests.post(url, data=data)
        flash('Dziękuję za wiadomość! Odpowiem wkrótce.', 'success')
    except Exception:
        flash('Błąd podczas wysyłania wiadomości.', 'danger')
    return redirect(url_for('main.index'))