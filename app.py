import os
from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_response(user_input, mode):
    prompts = {
        "press": "أنت خبير علاقات عامة. اكتب بيانًا صحفيًا احترافيًا باللغة العربية، يحتوي على عنوان جذاب، مقدمة، تفاصيل رئيسية، اقتباس رسمي، وخاتمة.",
        "customer": "أنت موظف علاقات عامة وخدمة عملاء محترف. اكتب ردًا مهذبًا وواضحًا واحترافيًا باللغة العربية على استفسار أو شكوى العميل.",
        "formal": "أنت كاتب إداري محترف. اكتب ردًا رسميًا مناسبًا للشركات والجهات الرسمية باللغة العربية.",
        "ideas": "أنت مستشار علاقات عامة. اقترح أفكار حملات علاقات عامة إبداعية وقابلة للتنفيذ باللغة العربية.",
        "crisis": "أنت خبير إدارة أزمات إعلامية. اكتب ردًا رسميًا هادئًا يحافظ على سمعة الجهة ويعالج الموقف باحتراف.",
        "social": "أنت متخصص محتوى رقمي. اكتب منشورًا احترافيًا وجذابًا لمنصات التواصل الاجتماعي باللغة العربية.",
        "email": "أنت كاتب مراسلات إدارية. اكتب بريدًا رسميًا احترافيًا باللغة العربية مناسبًا للشركات والجهات الرسمية."
    }

    system_prompt = prompts.get(mode, "أنت مساعد علاقات عامة محترف باللغة العربية.")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


@app.route("/", methods=["GET", "POST"])
def index():
    result = ""

    if request.method == "POST":
        user_input = request.form.get("user_input")
        mode = request.form.get("mode")

        if user_input:
            result = generate_response(user_input, mode)
        else:
            result = "الرجاء كتابة الطلب أولًا."

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)