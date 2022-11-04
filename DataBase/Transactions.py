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

    def __init__(self, bank_id, name):
        self.id = bank_id
        self.name = name


class Reasons(db_model):
    __table_name__ = "reasons"

    id = db_column(db.Integer, primary_key=True)
    name = db_column(db.String(10))
    transactions = db.relationship('MoneyTransactions', back_populates="reason")

    def __init__(self, reason_id, reason_name):
        self.id = reason_id
        self.name = reason_name


class Origins(db_model):
    __table_name__ = "origins"

    id = db_column(db.Integer, primary_key=True)
    name = db_column(db.String(10))
    transactions = db.relationship('MoneyTransactions', back_populates="origin")

    def __init__(self, origin_id, origin_name):
        self.id = origin_id
        self.name = origin_name


class Receivers(db_model):
    __table_name__ = "receivers"

    id = db_column(db.Integer, Sequence('seq_reg_id', start=1, increment=1), primary_key=True)
    name = db_column(db.String(25))
    transactions = db.relationship('MoneyTransactions', back_populates="receiver")
    country = db_column(db.String(25))
    relation_to_sender = db_column(db.String(25))

    def __init__(self, name, country, relation_to_sender):
        self.name = name
        self.country = country
        self.relation_to_sender = relation_to_sender


class MoneyTransactions(db_model):
    """
        Model for transactions list
    """
    __table_name__ = "money_transactions"

    id = db_column(db.Integer, Sequence('seq_reg_id', start=1, increment=1), primary_key=True)
    amount = db_column(db.Float)
    date = db_column(db.String(10))
    reference = db_column(db.String)

    reason_id = db.Column(db.Integer, db.ForeignKey('reasons.id'))
    reason = db.relationship('Reasons', back_populates="transactions")

    fee_id = db.Column(db.Integer, db.ForeignKey('fees.id'))
    fee = db.relationship('Fees', back_populates="transactions")

    bank_id = db.Column(db.Integer, db.ForeignKey('banks.id'))
    bank = db.relationship('Banks', back_populates="transactions")

    sender_ssn = db.Column(db.String, db.ForeignKey('senders.ssn'))
    sender = db.relationship('Senders', back_populates="transactions")

    receiver_id = db.Column(db.Integer, db.ForeignKey('receivers.id'))
    receiver = db.relationship('Receivers', back_populates="transactions")

    origin_of_money_id = db.Column(db.Integer, db.ForeignKey('origins.id'))
    origin = db.relationship('Origins', back_populates="transactions")

    # tr_ is transaction
    def __init__(self,
                 tr_amount,
                 tr_date,
                 tr_reference,
                 reason,
                 reason_id,
                 tr_fee,
                 bank_id,
                 bank,
                 sender_ssn,
                 sender,
                 receiver_id,
                 receiver,
                 origin_of_money_id,
                 origin_of_money
                 ):
        self.amount = tr_amount
        self.date = tr_date
        self.reference = tr_reference
        self.reason = reason
        self.reason_id = reason_id
        self.fee_id = tr_fee
        self.bank_id = bank_id
        self.sender_ssn = sender_ssn
        self.sender = sender
        self.bank = bank
        self.receiver = receiver
        self.receiver_id = receiver_id
        self.origin_of_money_id = origin_of_money_id
        self.origin_of_money = origin_of_money

    def __repr__(self):
        return '<Reference %r>' % self.reference
