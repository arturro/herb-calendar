from rest_framework import routers
from plants import views as plants_views

router = routers.DefaultRouter()
router.register(r'plant', plants_views.PlantViewSetCategoryViewSet)
