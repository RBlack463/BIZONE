from rest_framework import serializers
from .models import *


class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        if response['parent']:
            response['parent'] = Tree.objects.get(id=response['parent']).name
        return response


class TreeDetailSerializer(TreeSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        children = Tree.objects.filter(parent=obj.id)
        if children:
            return TreeDetailSerializer(children, many=True).data
        else:
            return []
