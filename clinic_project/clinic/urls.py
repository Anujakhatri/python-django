from .views import DoctorViewSet, PatientViewSet, AppointmentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('doctors', DoctorViewSet)
router.register('patients', PatientViewSet)
router.register('appointments', AppointmentViewSet)

urlpatterns = router.urls