from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from restaurante.models import Mesero

class MeseroListView(ListView):
    model = Mesero
    template_name = 'restaurante/mesero/list.html'


class MeseroCreateView(CreateView):
    model = Mesero
    template_name = "restaurante/mesero/form.html"
    fields = "__all__"
    success_url = "/restaurante/meseros"


class MeseroUpdateView(UpdateView):
    model = Mesero
    template_name = "restaurante/mesero/form.html"
    fields = "__all__"
    success_url = "/restaurante/meseros"


class MeseroDeleteView(DeleteView):
    model = Mesero
    success_url = "/restaurante/meseros"
