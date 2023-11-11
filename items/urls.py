from django.urls import path, include
from . import views
from core.views import get_cities
from rest_framework import routers
from .views import ItemViewSet

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)

app_name = 'items'

urlpatterns = [
   path('', views.browse, name='browse'),
   path('detail/<int:pk>/', views.detail, name='detail'),
   path('get_cities/', views.get_cities, name='get_cities'),
   path('new/', views.new, name='new'),
   path('<int:pk>/edit/', views.edit, name='edit'),
   path('<int:pk>/delete/', views.delete, name='delete'),
   path('api/', include(router.urls)),

]
