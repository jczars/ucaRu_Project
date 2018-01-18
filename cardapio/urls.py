from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('post/<int:pk>/', views.CardapioDetailView.as_view(), name='cardapio_detail'),
    path('post/new/', views.CardapioCreateView.as_view(), name='cardapio_new'),
    path('reserva/new/', views.ReservaCreateView.as_view(), name='reserva_new'),
    path('lista/', views.ReservaListView.as_view(), name='reserva_detail'),
]