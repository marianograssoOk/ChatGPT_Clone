from flask import Flask, request, render_template
from openai import OpenAI
import config
client = OpenAI(api_key=config.API_KEY)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

conversation_history = []

@app.route("/get")
def get_bot_response():
        userText = request.args.get('msg')
        conversation_history.append({"role": "user", "content": userText})
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=
                conversation_history,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=1
        )
        ai_response = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": ai_response})
        return ai_response

if __name__ == "__name__":
    app.run()