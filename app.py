from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
suggestions = []
app.secret_key = 'magic_secret'  # מפתח סודי – דרוש בשביל הודעות למשתמש

@app.route('/')
def index():
    return render_template('index.html')  # מציג את קובץ index.html שבתוך templates

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form.get('message')  # לוקח את ההודעה מהטופס
    if message:
        flash(f"הודעתך נקלטה: {message}")  # מציג את ההודעה למשתמש
    return redirect(url_for('index'))  # חוזר לדף הראשי


@app.route('/addNight', methods=['GET', 'POST'])
def question():
    if request.method == 'POST':
        user_question = request.form['addNight']
        suggestions.append(user_question)  # מוסיפה לרשימה
        return redirect(url_for('question'))  # רענון של הדף

    return render_template('addNight.html', suggestions=suggestions)

@app.route('/questions')# צפייה בהצעות
def show_questions():
    return render_template('questions.html', suggestions=suggestions)

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

