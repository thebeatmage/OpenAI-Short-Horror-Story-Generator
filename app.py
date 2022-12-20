import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        topic = request.form["topic"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(topic),
            temperature=0.6,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(topic):
    return """Topic: Breakfast
\nTwo-Sentence Horror Story: He always stops crying when I pour the milk on his cereal. I just have to remember not to let him see his face on the carton.
\n
\nTopic: Flatulence
\nTwo-Sentence Horror Story: The smell of sulfur filled the house, no matter how often I opened the windows. I realized too late that it was coming from inside me.
\n    
\nTopic: {}
\nTwo-Sentence Horror Story:
""".format(
        topic
    )
