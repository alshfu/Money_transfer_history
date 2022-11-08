class Transaction:
    # tr for transactions
    # def __init__(self, tr_date, tr_sender, tr_amount, tr_reason, tr_bank, tr_receiver, tr_id):
    def __init__(self, transaction):
        # self.tr_date = tr_date
        # self.tr_sender = tr_sender
        # self.tr_amount = tr_amount
        # self.tr_reason = tr_reason
        # self.tr_bank =  tr_bank
        # self.tr_receiver = tr_receiver
        # self.tr_id = tr_id
        self.transaction = transaction
        self.tr_date = self.get_tr_date()
        self.tr_sender = self.get_tr_sender()
        self.tr_amount = self.get_tr_amount()
        self.tr_reason = self.get_tr_reason()
        self.tr_bank = self.get_tr_bank()
        self.tr_receiver = self.get_tr_receiver()
        self.tr_id = self.get_tr_id()

    def get_tr_date(self):
        return self.transaction.date
