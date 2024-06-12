from rest_framework.permissions import  BasePermission
from django.contrib.auth.models import Group


def _is_in_group(user, group_name):
    """
    This function takes user and group as parameter and returns true if the user is present in that group
    """

    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist as e:
        return None


def _has_group_permission(user, required_group):
    """
    This function takes the user and checks if the user is in the list of group
    """
    return any([_is_in_group(user, group_name) for group_name in required_group])


class IsAmnex(BasePermission):
    required_group = ["Amnex"]
    """
    The function checks if the user has the required group permission.

    """

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(
            request.user, self.required_group)
        return request.user and has_group_permission
    


class IsBattery_IQ(BasePermission):
    required_group = ["Battery_IQ"]
    """
    The function checks if the user has the required group permission.

    """

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(
            request.user, self.required_group)
        return request.user and has_group_permission
    

class IsAchargeZone(BasePermission):
    required_group = ["chargeZone"]
    """
    The function checks if the user has the required group permission.

    """

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(
            request.user, self.required_group)
        return request.user and has_group_permission
    

class IsMBMT(BasePermission):
    required_group = ["MBMT"]
    """
    The function checks if the user has the required group permission.

    """

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(
            request.user, self.required_group)
        return request.user and has_group_permission