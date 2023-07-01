from django.test import TestCase


"""
Obtener los elementos del la clase - Tabla
1. Todos los elementos
query = NombreClase.objects.all()
2. Un elemento en particular
query = NombreCalse.objects.get(atributo='nombre_')

Crear un elemento
objecto = NombreClase(atributos....)
objecto.save()

Editar un elemento
elemento = NombreCalse.objects.get(atributo='nombre_')
elemento.atributo = 'Cambio que queremos hacer'
elemento.save()

Eliminar un elemento 
elemento = NombreClase.objects.get(atributo='nombre..')
elemento.delete()


Otras formas 
query = NombreClase.objects.filter(parametro de filtrado)
"""
