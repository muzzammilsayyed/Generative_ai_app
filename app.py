from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment variable
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    raise ValueError("The OPENAI_API_KEY environment variable is not set")

client = OpenAI(api_key=api_key)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('gpt.html')

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        prompt = request.form['userprompt']

        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=30
        )
        generated_text = response.choices[0].text

        return render_template("gpt.html", prompt=prompt, generated_text=generated_text)
    return render_template("gpt.html", prompt='', generated_text='')

@app.route('/img', methods=['GET', 'POST'])
def imggenerate():
    if request.method == 'POST':
        prompt = request.form['userprompt']

        response = client.images.generate(
            model="dall-e-2",
            prompt=prompt,
            size="256x256",
            quality="standard",
            n=1
        )
        image_url = response.data[0].url

        return render_template("gpt.html", prompt=prompt, image_url=image_url)
    return render_template("gpt.html", prompt='', image_url='')

if __name__ == '__main__':
    app.run(debug=True)
