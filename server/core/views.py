from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from rest_framework import viewsets
from .models import *
from .serializers import *


class DefaultModelViewSet(viewsets.ModelViewSet):
    model = None

    def get_queryset(self):
        self.queryset = self.model.objects.all()
        return super().get_queryset()


class TreeViewSet(DefaultModelViewSet):
    model = Tree
    serializer_class = TreeSerializer
    detail_serializer_class = TreeDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class

        return super(TreeViewSet, self).get_serializer_class()