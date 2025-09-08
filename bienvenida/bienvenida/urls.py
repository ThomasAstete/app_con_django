from django.contrib import admin
from django.urls import path, include
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', view.lista_productos, name='Productos'),
    path('inventario/', include('inventario.urls'))
]
