from rest_framework import generics
from .serializers import UserSerializer,RegisterSerializer,UserProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser

User=get_user_model()

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
    
    