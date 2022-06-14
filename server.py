from flask import Flask
from flask_migrate import Migrate
from models import db

from apis.login import login_view
from apis.cab import cab_view

from decouple import config


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"

db.init_app(app)
migrate = Migrate(app, db)


app.add_url_rule('/register', view_func=login_view.register,methods=['POST'])
app.add_url_rule('/login', view_func=login_view.login,methods=['POST'])
app.add_url_rule('/bookcab', view_func=cab_view.BookCab,methods=['POST'])
app.add_url_rule('/listbookings', view_func=cab_view.BookCab,methods=['GET'])




if __name__=='__main__':
    app.run(debug=config("DEBUG"))