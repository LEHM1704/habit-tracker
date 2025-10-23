from rest_framework.routers import DefaultRouter
from .views import HabitViewSet, HabitRecordViewSet

router = DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habit')
router.register(r'records', HabitRecordViewSet, basename='record')

urlpatterns = router.urls
