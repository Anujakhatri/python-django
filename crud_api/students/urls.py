from .views import StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter() # DefaultRouter is a class that automatically generates URLs for ViewSets.
router.register('students', StudentViewSet) # Create endpoints for StudentViewSet under /students/
urlpatterns = router.urls   #takes all of those magically generated URLs and hands them to Django.
