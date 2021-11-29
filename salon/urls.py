from django.urls import path
from .views import index, SalonCreateView

urlpatterns = [
    path('', index, name='index'),
    path('create/', SalonCreateView.as_view(), name='create'),
    # path('', SalonListView(), name='index'),
]