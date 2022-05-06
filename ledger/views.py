import logging

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ledger.models import Ledger
from ledger.serializer import LedgerSerializer
import ledger.service as ledger_service
from user.models import UserDetails
from user.service import get_user

logger = logging.getLogger('root')


class LedgerViewSet(viewsets.ModelViewSet):
    """This class provides Ledger CRUD functionalities"""

    serializer_class = LedgerSerializer
    queryset = Ledger.objects.all()

    def create(self, request, *args, **kwargs):
        """Create method for Ledger where user is explicitly related"""

        try:
            logger.debug('Create Ledger API called with data: {}'.format(request.data))
            user_id = self.kwargs['user_id']
            user = get_user(user_id)
            request.data['user'] = [user_id]
            return super().create(request)
        except ObjectDoesNotExist:
            return Response({'message': 'No such user'}, status=404)

    def list(self, request, *args, **kwargs):
        """Lists ledgers belonging to a particular user"""

        try:
            user_id = self.kwargs['user_id']
            logger.debug('list user ledgers API called for user with Id: {}'.format(user_id))
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
    """Splits the expense equally between multiple users."""

    logger.debug('Split expense API called.')
    return Response(ledger_service.split_expense(ledger_id, request.data))


@api_view(['POST'])
def load_pdf(request, user_id):
    """Loads transactions from bank pdf and create ledgers"""

    logger.debug('Load Pdf API called. File name: {}'.format(request.data["fileName"]))
    return Response(ledger_service.load_pdf(user_id,
                                            request.data["fileName"],
                                            request.data["password"]))
