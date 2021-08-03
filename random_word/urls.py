from django.urls import path
from . import views
# palabra/
urlpatterns = [
    path('', views.index ),
    path('reset/', views.resetear ),
    
]