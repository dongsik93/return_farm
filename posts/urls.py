from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name="index"),
    path('list/', views.list, name="list"),
    path('map/', views.map, name="map"),
    path('<int:id>/', views.detail, name="detail"),
]
 