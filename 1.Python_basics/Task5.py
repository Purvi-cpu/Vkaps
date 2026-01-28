from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/app', methods=['GET','POST'])
def home():
    name= None
    if request.method == 'POST':
        name = request.form.get('name')

    return render_template('greeting.html',name=name)

    
if __name__ == '__main__':
    app.run(debug=True)

