from django.core.exceptions import ValidationError
from django import forms
from restaurante.models import Orden, Mesero, Mesa, Plato, Cliente

class OrdenForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        label="Cliente",
        queryset=Cliente.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
        empty_label="Selecciona un cliente",
        required=False  # Permitir que sea opcional
    )

    mesero = forms.ModelChoiceField(
        label="Mesero",
        queryset=Mesero.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
        empty_label="Selecciona un mesero",
        required=True
    )

    mesa = forms.ModelChoiceField(
        label="Mesa",
        queryset=Mesa.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
        empty_label="Selecciona una mesa",
        required=True
    )

    platos = forms.ModelMultipleChoiceField(
        label="Platos",
        queryset=Plato.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Orden
        fields = ["cliente", "mesero", "mesa", "platos"]

    def clean(self):
        cleaned_data = super().clean()
        mesa = cleaned_data.get("mesa")

        if mesa:
            orden_abierta = Orden.objects.filter(mesa=mesa, estado="abierto")

            if self.instance.pk:
                orden_abierta = orden_abierta.exclude(pk=self.instance.pk)

            if orden_abierta.exists():
                raise ValidationError("La mesa ya tiene una orden abierta.")

        return cleaned_data

