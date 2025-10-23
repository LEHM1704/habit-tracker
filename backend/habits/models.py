from django.db import models

class Habit(models.Model):
    
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    FREQUENCY_CHOICES = [
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
        (MONTHLY, 'Monthly'),
    ]
    
    user=models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='habits')
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    frequency=models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default=DAILY)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    
    
    def __str__(self):
        return f"{self.name} ({self.user.username})"
    
    
class HabitRecord(models.Model):
    
    habit=models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='records')
    date=models.DateField()
    completed=models.BooleanField(default=False)
    note=models.TextField(blank=True)
    
    
    class Meta:
        unique_together = ('habit', 'date') #evita duplicados
    
    def __str__(self):
        return f"Record for {self.habit.name} on {self.date} - {'Completed' if self.completed else 'Not Completed'}"
