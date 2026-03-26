from flask import Flask, request, jsonify, render_template
from groq import Groq

app = Flask(__name__)

client = Groq(api_key="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")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_code():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "")

        chat = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Chỉ trả về code Python"},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.1-8b-instant"
        )

        return jsonify({"code": chat.choices[0].message.content})

    except Exception as e:
        return jsonify({"code": str(e)})

if __name__ == "__main__":
    app.run(debug=True)