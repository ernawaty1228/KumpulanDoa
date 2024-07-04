from django.urls import path
from .views import DoaList, DoaDetail

urlpatterns = [
    path('', DoaList.as_view(), name='doa-list'),
    path('<int:pk>/', DoaDetail.as_view(), name='doa-detail'),
]