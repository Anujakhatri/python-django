from .views import StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students', StudentViewSet)
urlpatterns = router.urls
