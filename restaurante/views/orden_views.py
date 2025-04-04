from django.shortcuts import render, redirect, get_object_or_404
from restaurante.forms import OrdenForm
from restaurante.models.orden import Orden

def orden_list(request):
    ordenes = Orden.objects.all()
    return render(request, "restaurante/orden/list.html", {"ordenes": ordenes})

def orden_create(request):
    form = OrdenForm()
    if request.method == "POST":
        form = OrdenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("orden_list")

    return render(request, "restaurante/orden/form.html", {"form": form})

def orden_edit(request, id):
    orden = get_object_or_404(Orden, id=id)
    if request.method == "POST":
        form = OrdenForm(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            return redirect("orden_list")

    form = OrdenForm(instance=orden)
    return render(request, "restaurante/orden/form.html", {"form": form})

def orden_delete(request, id):
    orden = get_object_or_404(Orden, id=id)
    orden.delete()
    return redirect("orden_list")
