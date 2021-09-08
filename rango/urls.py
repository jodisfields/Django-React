from django.urls import path
from . import views

urlpatterns = [
    path('api/rango/', views.RangoListCreate.as_view() ),
]