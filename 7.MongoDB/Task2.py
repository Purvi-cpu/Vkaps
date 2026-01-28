from flask import Flask, request, render_template
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
uri = os.getenv("MONGODB_URI")
client = MongoClient(uri)
db = client['db1']
collection = db["task2"]
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def Home():
    name = None
    email = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        document = {
            "name":name,
            "email":email
        }
        collection.insert_one(document)
        client.close()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
        
    
    

  



