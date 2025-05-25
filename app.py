# app.py

from flask import Flask, render_template, request
from markdown import markdown
from ai_engine import generate_text  # 여기 수정!

app = Flask(__name__)

@app.template_filter("markdown")
def markdown_filter(text):
    return markdown(text)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        result = generate_text(prompt)  # 여기 수정!
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)