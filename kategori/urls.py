from django.urls import path
from .views import KategoriList, KategoriDetail

urlpatterns = [
    path('', KategoriList.as_view(), name='kategori-list'),
    path('<int:pk>/', KategoriDetail.as_view(), name='kategori-detail'),
]
