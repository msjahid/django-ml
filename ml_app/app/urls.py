from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name='index'),
    path('predict/',views.predict,name='predict'),
]
