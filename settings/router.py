from rest_framework import routers

from app.views import StatViewSet
from shop.views import CategoryViewSet, ItemViewSet


router = routers.DefaultRouter()

router.register(r'stat',StatViewSet)
router.register(r'item',ItemViewSet)
router.register(r'category',CategoryViewSet)
