import requests
import os
from dotenv import load_dotenv
from flask import Flask, render_template
# import .env
load_dotenv()

API_KEY = os.getenv("NINJA_API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Check your .env file.")

API_URL = "https://api.api-ninjas.com/v1/quotes"

headers = {
    "X-Api-Key": API_KEY
}

app = Flask(__name__)

def generate_ai_quote():
    response = requests.get(API_URL, headers=headers)
    data = response.json()
    print(data)
    if isinstance(data, list) and len(data) > 0:
        quote = data[0]["quote"]
        author = data[0]["author"]
        return quote, author
    else:
        return "No quote received", "Unknown"

@app.route("/AI")
def index():
    quote, author = generate_ai_quote()
    return render_template(
        "index.html",
        quote1=quote,
        author1=author
    )

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/registration")
def register():
    return render_template('registration.html')

if __name__ == "__main__":
    app.run(debug=True)