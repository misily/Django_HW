from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from user import serializers
from rest_framework.generics import get_object_or_404

from user.models import User
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

class UserSignup(APIView):
    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입성공"}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response({"massage":f'${serializer.errors}'},status=status.HTTP_400_BAD_REQUEST)
   
    def get(self, request): #유저리스트
        users = User.objects.all()
        serializer = serializers.UserSerializer(users, many=True)
        return Response(serializer.data)


class UserManage(APIView):
    def put(self, request, user_id): #수정
        user = get_object_or_404(User, id=user_id)
        print(request.data)
        serializer = serializers.UserEditSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response('그 외')
    
    def delete(self, request, user_id): #탈퇴
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return Response("삭제됨")





