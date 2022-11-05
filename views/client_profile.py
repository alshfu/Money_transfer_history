import os

from flask import render_template, request, redirect, flash, url_for
from werkzeug.utils import secure_filename

from DataBase.DataBase import db
from DataBase.Sender import Senders
from DataBase.Transactions import MoneyTransactions
from config import UPLOAD_FOLDER


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
        return render_template("client_profile.html",
                               result=result,
                               amount_max=amount_max,
                               amount=amount,
                               transactions=transactions,
                               client=client)
    elif request.method == "POST":
        print("Profile page Updater")
        new_f_name = request.form.getlist("f_name")[0]
        new_l_name = request.form.getlist("l_name")[0]
        new_ssn = request.form.getlist("ssn")[0]
        new_e_mail = request.form.getlist("e_mail")[0]
        new_phone_n = request.form.getlist("phone_n")[0]
        new_expire_date = request.form.getlist("expire_date")[0]
        new_type_of_senders_document = request.form.getlist("type_of_senders_document")[0]
        # new_file_of_document = request.form.getlist("file_of_document")[0]
        #
        client = Senders.query.filter_by(id=request.form.getlist("id")[0]).one()
        client.ssn = new_ssn
        client.telefon = new_phone_n
        client.l_name = new_l_name
        client.f_name = new_f_name
        client.email = new_e_mail
        client.document.type_of_docs = new_type_of_senders_document
        client.document.expire_date = new_expire_date
        file = request.files['file_of_document']
        if file.filename != '':
            filename = secure_filename(file.filename)
            filename = new_ssn + "_" + new_expire_date + "_" + filename
            filename = filename.strip().replace("-", "_")
            file.save(os.path.join(UPLOAD_FOLDER + "/documents", filename))
            print(UPLOAD_FOLDER + "/documents/" + filename)
            client.document.file = UPLOAD_FOLDER + "/documents/" + filename
        db.session.commit()

        return redirect(request.referrer)
