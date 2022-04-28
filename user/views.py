import logging

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist, ValidationError

import user.service as user_service

logger = logging.getLogger('root')


@api_view(['POST'])
def create_user(request):
    """ Creates a new User."""

    try:
        new_user = user_service.create_user(request.data)
        return Response(new_user, status=201)
    except ValidationError as bad_request:
        return Response({'message': bad_request.message}, status=400)
    except Exception as ex:
        print(ex)


@api_view(['GET'])
def get(request, user_id):
    """Retrieves user details"""

    try:
        logger.info('Get user method called.')
        user_details = user_service.get_user(user_id)
        return Response(user_details)
    except ObjectDoesNotExist:
        return Response({'message': 'No such user'}, status=404)


@api_view(['GET'])
def get_all(request):
    """Retrieve all active users"""

    user_list = user_service.get_all_user()
    return Response(user_list)


@api_view(['PUT'])
def update(request, user_id):
    """Updates the existing user details"""

    try:
        updated_user = user_service.update_user(user_id, request.data)
        return Response(updated_user)
    except ObjectDoesNotExist:
        return Response({'message': 'No such user'}, status=404)
    except ValidationError as bad_request:
        return Response({'message': bad_request.message}, status=400)


@api_view(['DELETE'])
def delete_user(request, user_id):
    """Deleted the user"""

    try:
        user_service.delete_user(user_id)
        return Response(status=204)
    except ObjectDoesNotExist:
        return Response({'message': 'No such user'}, status=404)
