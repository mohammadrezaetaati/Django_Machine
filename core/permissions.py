from rest_framework.permissions import IsAuthenticated


class IsTechnician(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and\
               request.user.role == 'technician'


class IsInspector(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and\
               request.user.role == 'inspector'


class IsReception(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and\
               request.user.role == 'reception'
