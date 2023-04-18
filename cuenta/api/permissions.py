from rest_framework.permissions import BasePermission


class isAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.User.is_staff