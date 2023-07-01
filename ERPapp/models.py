from django.db import models
from django.utils.timezone import now

class Type(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre',unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name='Tipo'
        verbose_name_plural='Tipos'
        ordering=['id']

#DateField solo almacena la fecha dd/mm/yyyy
#DateField almacena fecha y hora
class Employee(models.Model):
    type = models.ForeignKey(Type, on_delete=models.SET_NULL,null=True)
    names = models.CharField(max_length=100, verbose_name='Nombre')
    last_name = models.CharField(max_length=50, verbose_name='Apellido')
    dni = models.CharField(max_length=20, unique=True, verbose_name='Documento de identificación')
    date_joined = models.DateField(default=now,verbose_name='Fecha de registro')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00,max_digits=8, decimal_places=2)
    state = models.BooleanField(default=True)
    image = models.ImageField(upload_to='avatar/%Y/%m/%d',null=True,blank=True)
    cv = models.FileField(upload_to='cv/%Y/%m/%d',null=True,blank=True)

    #Metodo __str__ muestra como se va ver representado el objeto al ser creado
    def __str__(self):
        return f'{self.names}  {self.last_name}'
    
    #Clase Meta permite personalizar varios aspectos del comportamiento del modelo
    class Meta:
        verbose_name='Empleado'
        verbose_name_plural='Empleados'
        db_table='empleado'
        ordering=['id']





