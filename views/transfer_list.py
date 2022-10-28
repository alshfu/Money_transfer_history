from flask import render_template

from DataBase.Transactions import MoneyTransactions


def transfer_list():
    print("Transfer List")
    result = []
    transaction_list = MoneyTransactions.query.all()
    for transaction in transaction_list:
        print(">>>>>>>>>>>>")
        print(transaction.amount)
        tr = {"amount": transaction.amount,
              "id": transaction.id,
              "date": transaction.date,
              "reference": transaction.reference,
              "reason": transaction.reason,
              "fee_id": transaction.fee_id,
              "bank": transaction.bank_id,
              "sender_ssn": transaction.sender_ssn}
        result.append(tr)

    return render_template("transfer_list.html", result=result)
