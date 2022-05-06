import datetime

import camelot

from ledger.models import Ledger
from ledger.serializer import LedgerSerializer
from user.service import get_user


def split_expense(ledger_id, split_data):
    ledger = Ledger.objects.get(pk=ledger_id)
    if not ledger.is_shared:
        split_data['total_amount'] = ledger.amount
        split_data['amount'] = ledger.amount/len(split_data['user'])
        split_data['is_shared'] = True
    else:
        split_data['amount'] = ledger.total_amount/len(split_data['user'])
    ledger = LedgerSerializer(ledger, data=split_data, partial=True)
    if ledger.is_valid(raise_exception=True):
        ledger.save()
        return ledger.data


def load_pdf(user_id, file_name, password):
    file_path = r"C:\Users\Admin\Documents\python\ExpenseManager\pdfs"
    file_path += ("\\" + file_name + ".pdf")
    user = get_user(user_id)

    file = camelot.read_pdf(file_path, password=password,
                            pages='all')
    for table in file:
        ledger_table = table.df
        for index, row in ledger_table.iterrows():
            ledger_data = {}
            if row[0] != "Date":
                ledger_data["name"] = row[1]
                ledger_data["category"] = 4
                date = row[0].split("/")
                date = datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
                ledger_data["date"] = date.strftime("%Y-%m-%d")
                ledger_data["description"] = "Bank Ref no: " + row[2]
                if float(row[4].replace(",", "")) == 0:
                    ledger_data["type"] = "Income"
                    ledger_data["amount"] = row[5].replace(",", "")
                else:
                    ledger_data["type"] = "Expense"
                    ledger_data["amount"] = row[4].replace(",", "")
                ledger_data['user'] = [user_id]
                ledger = LedgerSerializer(data=ledger_data)
                if ledger.is_valid(raise_exception=True):
                    ledger.save()
    return {"message": "Pdf loading successful"}
