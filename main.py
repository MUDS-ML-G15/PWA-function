from flask import Flask,render_template, request
app = Flask(__name__)

@app.route('/',methods=['POST'])

def hello(score=False):
    name = request.form['img']
    img="hogehuga"
    if score==True:
        score="休みましょう"
    else:
        pass
    return render_template('index.html',score=score) 

@app.route('/good')
def good():
    name = "Good"
    return name

## おまじない
if __name__ == "__main__":
    app.run(debug=True)