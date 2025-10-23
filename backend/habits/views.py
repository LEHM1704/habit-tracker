from rest_framework import viewsets, permissions
from .models import Habit, HabitRecord
from .serializers import HabitSerializer, HabitRecordSerializer

class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user).prefetch_related('records')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class HabitRecordViewSet(viewsets.ModelViewSet):
    serializer_class = HabitRecordSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    def get_queryset(self):
        return HabitRecord.objects.filter(habit__user=self.request.user).select_related('habit')