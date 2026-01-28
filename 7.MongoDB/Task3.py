from flask import Flask, request, render_template
import os
import openai
from dotenv import load_dotenv
from pymongo import MongoClient
from openai import OpenAI
from datetime import datetime

load_dotenv()
uri = os.getenv("MONGODB_URI")
mango_client = MongoClient(uri)
db = mango_client['db1']
collection = db["task3"]
hf_client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def text_generation():
    if request.method == 'POST':
        prompt = request.form.get('name')
        response = hf_client.chat.completions.create(
            model="deepseek-ai/DeepSeek-R1:novita",
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
        output_text = response.choices[0].message.content
        data = {
        "prompt": prompt,
        "output": output_text,
        "DateTime": datetime.utcnow()
    }
        collection.insert_one(data)
        mango_client.close()
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)