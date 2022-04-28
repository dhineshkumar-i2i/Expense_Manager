from ledger.models import Ledger
from ledger.serializer import LedgerSerializer


def split_expense(ledger_id, split_data):
    ledger = Ledger.objects.get(pk=ledger_id)
    if not ledger.is_shared:
        split_data['total_amount'] = ledger.amount
        split_data['amount'] = ledger.amount/len(split_data['users'])
        split_data['is_shared'] = True
    else:
        split_data['amount'] = ledger.total_amount/len(split_data['users'])
    ledger = LedgerSerializer(ledger, data=split_data, partial=True)
    if ledger.is_valid(raise_exception=True):
        ledger.save()
        return ledger.data
