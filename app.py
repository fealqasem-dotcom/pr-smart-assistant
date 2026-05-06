import os
from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_response(user_input, mode):
    prompts = {
        "press": "أنت خبير علاقات عامة. اكتب بيانًا صحفيًا احترافيًا باللغة العربية.",
        "customer": "أنت موظف خدمة عملاء محترف. رد بأسلوب لبق ورسمي.",
        "formal": "اكتب ردًا رسميًا احترافيًا مناسبًا للشركات.",
        "ideas": "اقترح أفكار حملات علاقات عامة إبداعية."
    }

    system_prompt = prompts.get(mode)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content


@app.route("/", methods=["GET", "POST"])
def index():

    result = ""

    if request.method == "POST":

        user_input = request.form["user_input"]
        mode = request.form["mode"]

        result = generate_response(user_input, mode)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)