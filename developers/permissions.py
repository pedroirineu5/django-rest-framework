from rest_framework import permission

# CLASSE MAIS COMUM PARA USAR AS PERMISSOES DO PERMISSION, BASTA CRIAR UMA UNICA CLASSE E PODER REUTILIZAR
class DevelopersPermissionClass(permission.BasePermission):
    def has_permission(self,request,view):
        return True