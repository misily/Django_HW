from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from todo.serializers import TodoSerializer, TodoCreateSerializer, TodoEditSerializer
from todo.models import Todo
from rest_framework.generics import get_object_or_404
from datetime import datetime
# Create your views here.


class TodoManage(APIView):
    def get(self, request):
        todoes = Todo.objects.all()
        serializer = TodoSerializer(todoes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request): #작성
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class TodoEdit(APIView):
    def put(self, request, todo_id):
        article = get_object_or_404(Todo, id=todo_id)
        if article.is_complete == True:
            article.completion_at = datetime.now()

        serializer = TodoEditSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
        

    def delete(self, request, todo_id): #삭제
        article = get_object_or_404(Todo, id=todo_id)
        article.delete()
        return Response("삭제됨")
