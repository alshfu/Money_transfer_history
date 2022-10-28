import os
from openpyxl import load_workbook
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for
from flask_login import login_required
from werkzeug.utils import secure_filename

from DataBase.DataBase import db
from DataBase.Transactions import MoneyTransactions, Senders
from config import ALLOWED_EXTENSIONS
from config import UPLOAD_FOLDER


@login_required
def xlsx_reader():
    if request.method == "POST":
        if 'transaktions_list' in request.form:
            print("IM hire")
            tr_list = request.form
            tr_date = tr_list["date"]
            print(request.args)
            print(tr_date)
            tr_bank = tr_list.getlist("bank")
            tr_sender_name = tr_list.getlist("senders_name")
            tr_senders_ssn = tr_list.getlist("senders_ssn")
            tr_senders_document = tr_list.getlist("senders_document")
            tr_senders_telefon = tr_list.getlist("telefon")
            tr_receiver_name = tr_list.getlist("receiver_name")
            tr_amount = tr_list.getlist("amount")
            tr_reason = tr_list.getlist("reason")
            tr_senders_address = tr_list.getlist("address")
            tr_receiver_name = tr_list.getlist("receiver_name")
            tr_reference = tr_list.getlist("reference")
            for i in range(len(tr_sender_name)):
                print(f"""{i}:{tr_date},{tr_bank},{tr_sender_name[i]},""")
                tr = MoneyTransactions(tr_amount=tr_amount[i],
                                       tr_reference=tr_reference[i],
                                       tr_reason=tr_reason[i],
                                       tr_fee="1",
                                       tr_date=tr_date,
                                       tr_bank_id=tr_bank[0],
                                       sender_ssn=tr_senders_ssn[i])
                tr_sender = Senders(l_name=tr_sender_name[i].split()[0],
                                    f_name=tr_sender_name[i].split()[1],
                                    ssn=tr_senders_ssn[i],
                                    se)
                db.session.add(tr)
                db.session.commit()
        else:
            print("Im not hre")

        if "xlsx_file" not in request.files:
            print("No file part")
            flash("No file part")
            return redirect(request.url)
        file = request.files["xlsx_file"]
        if file.filename == "":
            flash("No selected file")
            print("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            print(file.filename)
            data_from_file, file_date, total_amount = get_information_from_xlsx_file(
                UPLOAD_FOLDER + "/" + file.filename)
            # return redirect(url_for("xlsx_reader", data_from_file))
            return render_template("xlsx_reader.html", result=data_from_file, date=file_date, total_amount=total_amount)

    return render_template("xlsx_reader.html")


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def get_information_from_xlsx_file(file):
    wb = load_workbook(filename=file)
    ws = wb.active
    # print(ws.max_row)
    # print(ws.max_column)
    res = []
    datum = ws.cell(row=5, column=1).value
    total_amount = 0

    for i in range(1, ws.max_row + 1):
        if i > 18:
            # sender_name = ws.cell(row=i, column=1).value
            # receiver_name = ws.cell(row=i, column=3).value
            # reference = ws.cell(row=i, column=4).value
            total_amount = float(ws.cell(row=i, column=5).value) + total_amount
            # avi = ws.cell(row=i, column=6).value
            # address = ws.cell(row=i, column=7).value
            res.append(
                {
                    "id": str(i - 18),
                    "sender_name": ws.cell(row=i, column=1).value,
                    "receiver_name": ws.cell(row=i, column=3).value,
                    "reference": ws.cell(row=i, column=4).value,
                    "amount": ws.cell(row=i, column=5).value,
                    "avi": ws.cell(row=i, column=6).value,
                    "address": ws.cell(row=i, column=7).value,
                }
            )
    # for re in res:
    #     print(re)
    print(total_amount)
    return res, datum, total_amount


if __name__ == "__main__":
    pass
