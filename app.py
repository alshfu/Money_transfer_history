from flask import Flask
from flask import redirect
from DataBase.DataBase import db
from views.client_list import client_list
from views.client_profile import client_profile
from views.transfer_list import transfer_list
from views.xlsx_reader import xlsx_reader
from views.login import login_manager
from views.login import logout
from views.login import login

# import declared routes
app = Flask(__name__)
app.config.from_pyfile('config.py')
login_manager.init_app(app)
db.init_app(app)

app.add_url_rule('/', view_func=xlsx_reader, methods=['GET', 'POST'])
app.add_url_rule('/xlsx_reader', view_func=xlsx_reader, methods=['GET', 'POST'])
app.add_url_rule('/transfer_list', view_func=transfer_list, methods=['GET', 'POST'])
app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])
app.add_url_rule('/client_list', view_func=client_list, methods=['GET', 'POST'])
app.add_url_rule('/client_profile', view_func=client_profile, methods=['GET', 'POST'])
app.add_url_rule('/logout', view_func=logout)

with app.app_context():
    db.create_all()


@app.errorhandler(401)
def custom_401(error):
    print(error)
    return redirect('/login')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
