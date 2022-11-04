from flask import render_template, request

from DataBase.Transactions import MoneyTransactions


def transfer_list():
    result = []
    if request.method == "POST":
        if 'search' in request.form:
            search_request = request.form.getlist("search")[0].replace(" ","")
            search_value_by_ssn = MoneyTransactions.query.filter_by(sender_ssn=search_request).all()
            search_value_by_amount = MoneyTransactions.query.filter_by(amount=search_request).all()
            search_value_by_date = MoneyTransactions.query.filter_by(date=search_request).all()
            search_value_by_reference = MoneyTransactions.query.filter_by(reference=search_request).all()
            if len(search_value_by_ssn) != 0:
                transaction_list = search_value_by_ssn
            elif len(search_value_by_amount) != 0:
                transaction_list = search_value_by_amount
            elif len(search_value_by_date) != 0:
                transaction_list = search_value_by_date
            else:
                transaction_list = search_value_by_reference



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

    return render_template("transfer_list.html", result=result)
