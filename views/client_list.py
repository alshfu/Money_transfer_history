from flask import render_template, request

from DataBase.Sender import Senders
from DataBase.Transactions import MoneyTransactions

def client_list():
    result = []
    total_amount = 0
    if request.method == "POST":
        if 'search' in request.form:
            search_value_by_ssn = Senders.query.filter_by(ssn=request.form.getlist("search")[0]).all()
            if len(search_value_by_ssn) != 0:
                clients_list = search_value_by_ssn
    else:
        clients_list = Senders.query.all()
    for client in clients_list:
        result.append(client)


    return render_template("client_list.html", result=result)
