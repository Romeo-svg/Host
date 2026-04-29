from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
CORS(app)

# 🔐 PUT YOUR EMAIL DETAILS HERE
EMAIL_USER = "yourgmail@gmail.com"
EMAIL_PASS = "uwky ygxx ceuu syei"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-rsvp', methods=['POST'])
def rsvp():
    try:
        data = request.get_json()
        guest_name = data.get('name')
        guest_email = data.get('email')

        msg = EmailMessage()
        msg['Subject'] = f'💍 RSVP: {guest_name}'
        msg['From'] = EMAIL_USER
        msg['To'] = EMAIL_USER

        msg.set_content(
            f"New RSVP Confirmation!\n\n"
            f"Name: {guest_name}\n"
            f"Email: {guest_email}\n"
            f"Message: I'll attend 🎉"
        )

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)

        return jsonify({"status": "success", "message": f"Confirmed! See you there, {guest_name} 🎉"})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"status": "error", "message": "Error sending RSVP"}), 500


if __name__ == "__main__":
    app.run(debug=True)