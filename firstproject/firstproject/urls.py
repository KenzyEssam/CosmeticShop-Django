from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('otherpages/', include('otherpages.urls')),
    path('home/', include('home.urls')),
    path('ccart/', include('ccart.urls')),
    path('register/', include('register.urls')),
    path('product/', include('product.urls')),

]
