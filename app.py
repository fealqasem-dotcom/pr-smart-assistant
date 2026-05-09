from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_response(user_input, mode):

    prompts = {

        "summary":
        f"لخص النص التالي بالعربية بشكل واضح ومختصر:\n\n{user_input}",

        "rewrite":
        f"أعد صياغة النص التالي بطريقة احترافية:\n\n{user_input}",

        "translate":
        f"ترجم النص التالي إلى الإنجليزية:\n\n{user_input}",

        "email":
        f"اكتب بريد إلكتروني احترافي بناءً على النص التالي:\n\n{user_input}",

        "content":
        f"اعطني أفكار محتوى بناءً على الموضوع التالي:\n\n{user_input}",

        "explain":
        f"اشرح الموضوع التالي بطريقة مبسطة:\n\n{user_input}"
    }

    prompt = prompts.get(mode, user_input)

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


@app.route("/", methods=["GET", "POST"])
def index():

    result = ""

    if request.method == "POST":

        user_input = request.form.get("user_input")
        mode = request.form.get("mode")

        if user_input:

            result = generate_response(
                user_input,
                mode
            )

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)