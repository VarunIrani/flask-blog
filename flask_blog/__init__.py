from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from hush import SECRET_KEY

app = Flask(__name__)

# Used to encrypt cookies and save them in the browser. Shhh! Don't tell anyone
app.config['SECRET_KEY'] = SECRET_KEY

# URI to the local sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Create a SQLite database instance
db = SQLAlchemy(app)

from flask_blog import routes
