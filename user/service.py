from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.paginator import Paginator

from user.models import UserDetails
from user.serializer import UserSerializer


def create_user(new_user_data):
    """Validates and created a new user."""

    new_user = UserSerializer(data=new_user_data)
    new_user.is_valid(raise_exception=True)
    new_user.save()
    return new_user.data


def get_user(user_id):
    """retrieves a user if the user is active"""

    user_details = UserDetails.objects.get(pk=user_id)
    if user_details.is_active:
        user_details = UserSerializer(user_details)
        return user_details.data
    else:
        raise ObjectDoesNotExist()


def get_all_user():
    """Returns a paginated list of all users."""

    paginator = Paginator(UserDetails.objects.all().filter(is_active=True), 20)
    users = paginator.get_page(1)
    user_list = UserSerializer(instance=users, many=True)
    return user_list.data


def update_user(user_id, user_details):
    """Validates the data and updates a user."""

    old_user_data = UserDetails.objects.get(pk=user_id)
    if not old_user_data.is_active:
        raise ObjectDoesNotExist()
    updated_user_data = UserSerializer(old_user_data,
                                       data=user_details, partial=True)
    if updated_user_data.is_valid(raise_exception=True):
        updated_user_data.save()
    return updated_user_data.data


def delete_user(user_id):
    """Makes a user inActive."""

    user = UserDetails.objects.get(pk=user_id)
    user.is_active = False
    user.save()
