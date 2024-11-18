from django.shortcuts import render
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, UserChangeSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
# Create your views here.

@api_view(["GET", "PUT"])
def profile(request,user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = UserChangeSerializer(user,data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data)
