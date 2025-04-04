from django.urls import path

from . import views
from .views import orden_list, orden_create, orden_edit, orden_delete, orden_close

urlpatterns = [

    path("clientes", views.ClienteListView.as_view(), name="clientes"),
    path("clientes/create", views.ClienteCreateView.as_view(), name="cliente_create"),
    path("clientes/editar/<int:pk>", views.ClienteUpdateView.as_view(), name="cliente_editar"),
    path('clientes/<int:pk>/delete', views.ClienteDeleteView.as_view(), name='cliente_delete'),

    path("platos", views.PlatoListView.as_view(), name="platos"),
    path("platos/create", views.PlatoCreateView.as_view(), name="platos_create"),
    path("platos/editar/<int:pk>", views.PlatoUpdateView.as_view(), name="platos_editar"),
    path('platos/<int:pk>/delete', views.PlatoDeleteView.as_view(), name="platos_delete"),

    path("meseros", views.MeseroListView.as_view(), name="meseros"),
    path("meseros/create", views.MeseroCreateView.as_view(), name="meseros_create"),
    path("meseros/editar/<int:pk>", views.MeseroUpdateView.as_view(), name="meseros_editar"),
    path('meseros/<int:pk>/delete', views.MeseroDeleteView.as_view(), name="meseros_delete"),

    path("mesas", views.MesaListView.as_view(), name="mesas"),
    path("mesas/create", views.MesaCreateView.as_view(), name="mesas_create"),
    path("mesas/editar/<int:pk>", views.MesaUpdateView.as_view(), name="mesas_editar"),
    path('mesas/<int:pk>/delete', views.MesaDeleteView.as_view(), name="mesas_delete"),

    #me quede haciendo lo de ordenes acabar
    path("ordenes", orden_list, name="orden_list"),
    path("ordenes/create", orden_create, name="orden_create"),
    path("ordenes/<int:id>/editar", orden_edit, name="orden_edit"),
    path("ordenes/<int:id>/eliminar", orden_delete, name="orden_delete"),
    path("ordenes/<int:id>/cerrar/", orden_close, name="orden_close"),
#agregando cambios

]