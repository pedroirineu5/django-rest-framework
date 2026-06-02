from rest_framework import permissions

# CLASSE MAIS COMUM PARA USAR AS PERMISSOES DO PERMISSION, BASTA CRIAR UMA UNICA CLASSE E PODER REUTILIZAR
class DevelopersPermissionClass(permissions.BasePermission):
    def has_permission(self,request,view):
        return True