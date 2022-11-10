from DataBase.DataBase import db_model, db_column, db


class Documents(db_model):
    __table_name__ = "documents"

    id = db_column(db.Integer, primary_key=True)
    type_of_docs = db_column(db.String(10))
    expire_date = db_column(db.String(10))
    file = db_column(db.String())
    senders = db.relationship('Senders', back_populates="document")

    def __init__(self,
                 type_of_docs,
                 expire_date,
                 file):
        self.type_of_docs = type_of_docs
        self.expire_date = expire_date
        self.file = file


class Senders(db_model):
    __table_name__ = "senders"

    id = db_column(db.Integer, primary_key=True)
    f_name = db_column(db.String(20))
    l_name = db_column(db.String(20))
    ssn = db_column(db.String(13), unique=True)
    telefon = db_column(db.String(13))
    email = db_column(db.String(13))
    address = db_column(db.Text())
    transactions = db.relationship('MoneyTransactions', back_populates="sender")

    document = db.relationship('Documents', back_populates="senders")
    document_id = db.Column(db.Integer, db.ForeignKey('documents.id'))

    def __init__(self, f_name, l_name, ssn, phone_number, address, document, document_id):
        self.l_name = l_name
        self.ssn = ssn
        self.f_name = f_name
        self.telefon = phone_number
        self.email = "alsh@gmail.com"
        print(address)
        self.address = address
        self.document = document
        self.document_id = document_id
