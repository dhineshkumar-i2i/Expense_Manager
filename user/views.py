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
        logger.debug('Create user API called. \nData: {}'.format(request.data))
        new_user = user_service.create_user(request.data)
        logger.debug('User created. Id: {}'.format(new_user['id']))
        return Response(new_user, status=201)
    except ValidationError as bad_request:
        logger.debug('validation Error, Invalid inputs')
        return Response({'message': bad_request.message}, status=400)
    except Exception as ex:
        print(ex)


@api_view(['GET'])
def get(request, user_id):
    """Retrieves user details"""

    try:
        logger.debug('Get user API called for Id {}'.format(user_id))
        user_details = user_service.get_user(user_id)
        return Response(user_details)
    except ObjectDoesNotExist:
        logger.debug('No user exists for Id {}'.format(user_id))
        return Response({'message': 'No such user'}, status=404)


@api_view(['GET'])
def get_all(request):
    """Retrieve all active users"""

    logger.debug('List users method called.')
    user_list = user_service.get_all_user()
    return Response(user_list)


@api_view(['PUT'])
def update(request, user_id):
    """Updates the existing user details"""

    try:
        logger.debug('Update user API called with data {}'.format(request.data))
        updated_user = user_service.update_user(user_id, request.data)
        return Response(updated_user)
    except ObjectDoesNotExist:
        logger.debug('No user exists for Id {}'.format(user_id))
        return Response({'message': 'No such user'}, status=404)
    except ValidationError as bad_request:
        logger.debug('validation Error, Invalid inputs')
        return Response({'message': bad_request.message}, status=400)


@api_view(['DELETE'])
def delete_user(request, user_id):
    """Deleted the user"""

    try:
        logger.debug('Delete user API called for userId : {}'.format(user_id))
        user_service.delete_user(user_id)
        return Response(status=204)
    except ObjectDoesNotExist:
        logger.debug('No user exists for Id {}'.format(user_id))
        return Response({'message': 'No such user'}, status=404)
