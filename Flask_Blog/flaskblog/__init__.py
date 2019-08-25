
# this file tells python that this is a package

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# important
# secrets.token_hex(16)
app.config['SECRET_KEY'] = 'beaadd39d35e24a7746cce7a6397632a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes
