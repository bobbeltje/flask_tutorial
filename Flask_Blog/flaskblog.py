
from flask import Flask
app = Flask(__name__)

# add a second decorator to have both pointing at the same thing
@app.route('/')
@app.route('/home')
def home():
    return '<h1>Home Page</h1>'
   
@app.route('/about')
def about():
    return '<h1>About Page</h1>'

# to run the app without setting environmental variables
if __name__ == '__main__':
    app.run(debug=True)
