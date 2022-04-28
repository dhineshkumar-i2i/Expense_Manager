from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ledger.models import Ledger
from ledger.serializer import LedgerSerializer
import ledger.service as ledger_service
from user.models import UserDetails
from user.service import get_user


class LedgerViewSet(viewsets.ModelViewSet):
    """This class provides Ledger CRUD functionalities"""

    serializer_class = LedgerSerializer
    queryset = Ledger.objects.all()

    def create(self, request, *args, **kwargs):
        """Create method for Ledger where user is explicitly related"""

        try:
            user_id = self.kwargs['user_id']
            user = get_user(user_id)
            request.data['users'] = [user_id]
            return super().create(request)
        except ObjectDoesNotExist:
            return Response({'message': 'No such user'}, status=404)

    def list(self, request, *args, **kwargs):
        """Lists ledgers belonging to a particular user"""

        try:
            user_id = self.kwargs['user_id']
            user = get_user(user_id)
            return Response(user['ledger'])
        except ObjectDoesNotExist:
            return Response({'message': 'No such user'}, status=404)

    def retrieve(self, request, *args, **kwargs):
        """Retrieving a particular ledger details"""

        try:
            user_id = self.kwargs['user_id']
            user = get_user(user_id)
            ledger_id = self.kwargs['pk']
            ledger = Ledger.objects.get(pk=ledger_id)
            ledger = LedgerSerializer(ledger)
            return Response(ledger.data)
        except UserDetails.DoesNotExist:
            return Response({'message': 'No such user'}, status=404)
        except Ledger.DoesNotExist:
            return Response({'message': 'No such Expense or Income'},
                            status=404)


@api_view(['PUT'])
def split_expense(request, user_id, ledger_id):
    """Split the expense equally between multiple users."""

    return Response(ledger_service.split_expense(ledger_id, request.data))
