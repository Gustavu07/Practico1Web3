from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from restaurante.models import Cliente

class ClienteListView(ListView):
    model = Cliente
    template_name = 'restaurante/cliente/list.html'


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = "restaurante/cliente/form.html"
    fields = "__all__"
    success_url = "/restaurante/clientes"


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = "restaurante/cliente/form.html"
    fields = "__all__"
    success_url = "/restaurante/clientes"


class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = "/restaurante/clientes"
