from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('naive/', views.NaiveAPIView.as_view(), name='uuid-detail'),
    path('cached/', views.CachedAPIView.as_view(), name='cache-implementation')
]
