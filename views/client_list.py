from flask import render_template, request

from DataBase.Sender import Senders

def client_list():
    result = []
    clients_list=[]
    if request.method == "POST":
        if 'search' in request.form:
            search_value_by_ssn = Senders.query.filter_by(ssn=request.form.getlist("search")[0]).all()
            if len(search_value_by_ssn) != 0:
                clients_list = search_value_by_ssn
    else:
        clients_list = Senders.query.all()
    for client in clients_list:
        result.append(client)

    clients_list.clear()
    for elem in result:
        print(elem.f_name)

    return render_template("client_list.html", result=result)
