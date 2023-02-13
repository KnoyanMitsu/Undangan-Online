from django.conf.urls import url
from dataKendaraan import views
from django.urls import path

urlpatterns = [
    path('kendaraan/', views.kendaraan_list),
    path('kendaraan/<int:pk>/', views.kendaraan_detail),
]
