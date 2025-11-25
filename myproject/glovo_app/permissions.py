from rest_framework.permissions import BasePermission

class CheckRolePermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'client'

class CourierPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'courier'

class CreateStorePermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'owner'