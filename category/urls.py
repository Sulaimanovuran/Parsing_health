from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.CategoryViewSet, basename='category')


urlpatterns = [
    # path('create/', views.PersonViewSet.as_view()),
    path('', include(router.urls))

]