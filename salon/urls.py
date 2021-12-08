from django.urls import path
from .views import (SalonListView, ServisListView, create_salon, RecordListView,
                    RecordDetailView, delete_post, RecordUpdateView)


urlpatterns = [
    path('', SalonListView.as_view(), name='index'),
    path('services/', ServisListView.as_view(), name='servis'),
    path('detail/<int:pk>/', RecordDetailView.as_view(), name='detail'),
    path('create/', create_salon, name='create'),
    path('delete/<int:pk>/', delete_post, name='delete'),
    path('record/', RecordListView.as_view(), name='records'),
    path('update-post/<int:pk>/', RecordUpdateView.as_view(), name='update'),
]