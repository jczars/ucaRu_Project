from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from . models import Cardapio, Reserva

class HomeListView(ListView):
    model = Cardapio
    template_name = 'home.html'

class CardapioDetailView(DetailView):
    model = Cardapio
    template_name = 'cardapio_detail.html'

class CardapioCreateView(CreateView):
    model = Cardapio
    template_name = 'cardapio_new.html'
    fields = '__all__'

class ReservaCreateView(CreateView):
    model = Reserva
    template_name = 'reserva_new.html'
    fields = '__all__'

class ReservaListView(ListView):
    model = Reserva
    template_name = 'reserva_detail.html'
