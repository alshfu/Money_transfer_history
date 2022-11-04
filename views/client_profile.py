from flask import render_template, request

from DataBase.Sender import Senders
from DataBase.Transactions import MoneyTransactions


def client_profile():
    result = []
    if request.method == "GET":
        ssn = request.args.get("ssn")
        amount = 0
        amounts = []
        amount_max = ''
        print(ssn)
        search_value_by_ssn = Senders.query.filter_by(ssn=ssn).all()
        if len(search_value_by_ssn) != 0:
            client = search_value_by_ssn[0]
            transactions = MoneyTransactions.query.filter_by(sender_ssn=ssn).all()
            for tr in transactions:
                amount += float(tr.amount)
                amounts.append(tr.amount)
            amount_max = max(amounts)
            # document = Senders.query.filter_by(ssn=ssn).all()

    return render_template("client_profile.html",
                           result=result,
                           amount_max=amount_max,
                           amount=amount,
                           transactions=transactions,
                           client=client)
