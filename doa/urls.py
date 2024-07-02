from django.urls import path
from .views import DoaList, DoaDetail

urlpatterns = [
    path('doa/', DoaList.as_view(), name='doa-list'),
    path('doa/<int:pk>/', DoaDetail.as_view(), name='doa-detail'),
]