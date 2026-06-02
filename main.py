from flask import Flask,render_template,request,jsonify,url_for
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

app=Flask(__name__)

load_dotenv()
api_key=os.getenv("api_key_gemini")

client=genai.Client(api_key=api_key)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/query",methods=["POST"])
def gpt():
    data=request.get_json()
    user_query=data.get("query")
    response=client.models.generate_content(
        model="gemini-3.5-flash",
        contents=user_query,

        config=types.GenerateContentConfig(
            system_instruction="Act as a personal assistant ",
            temperature=0.6,
            max_output_tokens=2048
        )
    )
    ans=response.text.strip()
    return jsonify({"response":ans}),200


if (__name__)=="__main__":
    app.run(debug=True)
