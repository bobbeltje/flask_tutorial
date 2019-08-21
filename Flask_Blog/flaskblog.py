
from flask import Flask, render_template, url_for
app = Flask(__name__)

# dummy data, usually you would get this from a database
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

# add a second decorator to have both pointing at the same thing
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)
   
@app.route('/about')
def about():
    return render_template('about.html', title='About')

# to run the app without setting environmental variables
if __name__ == '__main__':
    app.run(debug=True)
