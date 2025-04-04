from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from restaurante.models import Plato

class PlatoListView(ListView):
    model = Plato
    template_name = 'restaurante/platos/list.html'


class PlatoCreateView(CreateView):
    model = Plato
    template_name = "restaurante/platos/form.html"
    fields = "__all__"
    success_url = "/restaurante/platos"


class PlatoUpdateView(UpdateView):
    model = Plato
    template_name = "restaurante/platos/form.html"
    fields = "__all__"
    success_url = "/restaurante/platos"


class PlatoDeleteView(DeleteView):
    model = Plato
    success_url = "/restaurante/platos"
