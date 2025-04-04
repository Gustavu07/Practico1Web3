# views.py
from django.shortcuts import render, redirect, get_object_or_404
from restaurante.forms import CerrarOrdenForm
from restaurante.models.orden import Orden

def orden_close(request, id):
    orden = get_object_or_404(Orden, id=id)

    if request.method == "POST":
        form = CerrarOrdenForm(request.POST, instance=orden)
        if form.is_valid():
            orden = form.save(commit=False)
            orden.estado = "cerrado"
            orden.save()
            return redirect("orden_list")

    form = CerrarOrdenForm(instance=orden)
    return render(request, "restaurante/orden/cerrar_orden.html", {"form": form, "orden": orden})
