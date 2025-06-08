# Personal CV Website

This project is a personal CV website built using Flask. It showcases personal information, skills, education, work experience, and languages in a structured format.  
Includes a contact form that sends messages directly to your Telegram via a bot, and a button to download your CV as a PDF.

## Project Structure

```
cv-python-flask
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── templates
│   │   └── index.html
│   └── static
│       ├── style.css
│       └── Dorofii_Karnaukh_CV.pdf
├── requirements.txt
├── run.py
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/dorofi/cv-python-flask.git
   cd cv-python-flask
   ```

2. **(Optional) Create and activate a virtual environment:**
   ```
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure your Telegram bot:**
   - Create a bot via [@BotFather](https://t.me/BotFather) and get your token.
   - Get your chat_id (write to your bot and check `/getUpdates`).
   - Set `TELEGRAM_TOKEN` and `TELEGRAM_CHAT_ID` in `app/routes.py`.

5. **Add your PDF CV:**
   - Place your PDF file (e.g., `Dorofii_Karnaukh_CV.pdf`) in the `app/static/` folder.

6. **Run the application:**
   ```
   python run.py
   ```

7. **Open your web browser and go to:**
   ```
   http://127.0.0.1:5000
   ```

## Features

- Modern responsive design
- Downloadable PDF CV
- Contact form with Telegram integration (messages go directly to your Telegram)
- Flash messages with auto-hide

## Technologies

- Python 3.11+
- Flask 2.2.2
- Gunicorn
- Jinja2
- requests

## Author

Dorofii Karnaukh  
[GitHub](https://github.com/dorofi)

---

Feel free to customize the content and styles to better reflect your personal brand!