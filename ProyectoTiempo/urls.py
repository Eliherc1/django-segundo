
from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('time_display.urls')),
    path('palabra/', include('random_word.urls')),
    
]
