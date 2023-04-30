from rest_framework import serializers
from todo.models import Todo
from datetime import datetime

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title',)

class TodoEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title','is_complete')