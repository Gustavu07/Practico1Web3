from django import forms
from restaurante.models import Orden , Cliente


class CerrarOrdenForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        label="Cliente",
        queryset=Cliente.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
        empty_label="Selecciona un cliente",
        required=True
    )

    class Meta:
        model = Orden
        fields = ["cliente"]
