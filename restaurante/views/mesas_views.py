from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from restaurante.models import Mesa

class MesaListView(ListView):
    model = Mesa
    template_name = 'restaurante/Mesa/list.html'


class MesaCreateView(CreateView):
    model = Mesa
    template_name = "restaurante/Mesa/form.html"
    fields = "__all__"
    success_url = "/restaurante/mesas"


class MesaUpdateView(UpdateView):
    model = Mesa
    template_name = "restaurante/Mesa/form.html"
    fields = "__all__"
    success_url = "/restaurante/mesas"


class MesaDeleteView(DeleteView):
    model = Mesa
    success_url = "/restaurante/mesas"
