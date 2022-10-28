from sqlalchemy import Sequence

from DataBase.DataBase import db_model, db_column, db


def im_hire(data=""):
    print("Im hire with data: ", data)


class Fees(db_model):
    __table_name__ = "fees"
    id = db_column(db.Integer, primary_key=True)
    value = db_column(db.Float)
    transactions = db.relationship('MoneyTransactions', back_populates="fee")

    def __init__(self, fee_value):
        self.value = fee_value


class Banks(db_model):
    __table_name__ = "banks"

    id = db_column(db.Integer, primary_key=True)
    name = db_column(db.String(10))
    transactions = db.relationship('MoneyTransactions', back_populates="bank")

    def __init__(self, bank_name):
        self.name = bank_name


def create_simple_transaction():
    if MoneyTransactions.query.filter_by(id='0').first() is None:
        pass
    if Fees.query.filter_by(value='0.23').first() is None:
        im_hire(Fees.query.filter_by(value='0.23').first())
        fee = Fees(fee_value=0.23)
        db.session.add(fee)
        db.session.commit()
    else:
        im_hire(Fees.query.filter_by(value='0.23').first())

    if Banks.query.filter_by(name='Nordea').first() is None:
        bank_nordea = Banks(bank_name="Nordea")
        bank_handels_banken = Banks(bank_name="Handelsbanken")

        db.session.add(bank_nordea)
        db.session.add(bank_handels_banken)
        db.session.commit()


class MoneyTransactions(db_model):
    __table_name__ = "money_transactions"

    id = db_column(db.Integer, Sequence('seq_reg_id', start=1, increment=1), primary_key=True)
    amount = db_column(db.Float)
    date = db_column(db.String(10))
    reference = db_column(db.String)
    reason = db_column(db.String)

    fee_id = db.Column(db.Integer, db.ForeignKey('fees.id'))
    fee = db.relationship('Fees', back_populates="transactions")

    bank_id = db.Column(db.Integer, db.ForeignKey('banks.id'))
    bank = db.relationship('Banks', back_populates="transactions")

    sender_ssn = db.Column(db.String, db.ForeignKey('senders.ssn'))
    sender = db.relationship('Senders', back_populates="transactions")

    # tr_ is transaction
    def __init__(self, tr_amount, tr_date, tr_reference, tr_reason, tr_fee, tr_bank_id, sender_ssn):
        self.amount = tr_amount
        self.date = tr_date
        self.reference = tr_reference
        self.reason = tr_reason
        self.fee_id = tr_fee
        self.bank_id = tr_bank_id
        self.sender_ssn = sender_ssn


class Senders(db_model):
    __table_name__ = "senders"

    id = db_column(db.Integer, primary_key=True)
    f_name = db_column(db.String(20))
    l_name = db_column(db.String(20))
    ssn = db_column(db.String(13), unique=True)
    telefon = db_column(db.String(13), unique=True)
    email = db_column(db.String(13), unique=True)

    transactions = db.relationship('MoneyTransactions', back_populates="sender")

    def __init__(self, f_name, l_name, ssn, phone_number):
        self.l_name = l_name,
        self.ssn = ssn,
        self.f_name = f_name,
        self.telefon = phone_number


if __name__ == "__main__":
    pass
    create_simple_transaction()
