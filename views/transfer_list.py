from flask import render_template, request

from DataBase.Transactions import MoneyTransactions


def transfer_list():
    result = []
    transaction_list = []
    if request.method == "POST":
        if 'search' in request.form:
            search_request = request.form.getlist("search")[0].replace(" ", "")
            if len(MoneyTransactions.query.filter_by(sender_ssn=search_request).all()) != 0:
                transaction_list = MoneyTransactions.query.filter_by(sender_ssn=search_request).all()
            elif len(MoneyTransactions.query.filter_by(amount=search_request).all()) != 0:
                transaction_list = MoneyTransactions.query.filter_by(amount=search_request).all()
            elif len(MoneyTransactions.query.filter_by(date=search_request).all()) != 0:
                transaction_list = MoneyTransactions.query.filter_by(date=search_request).all()
            else:
                transaction_list = MoneyTransactions.query.filter_by(reference=search_request).all()
    else:
        transaction_list = MoneyTransactions.query.all()

    for transaction in transaction_list:
        tr = {"amount": transaction.amount,
              "id": transaction.id,
              "date": transaction.date,
              "reference": transaction.reference,
              "reason": transaction.reason.name,
              "receiver": transaction.receiver,
              "fee_id": transaction.fee_id,
              "origin": transaction.origin,
              "bank": transaction.bank.name,
              "sender": transaction.sender}
        result.append(tr)
    transaction_list.clear()
    return render_template("transfer_list.html", result=result)
