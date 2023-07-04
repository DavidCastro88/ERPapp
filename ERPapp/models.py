from django.db import models
from django.utils.timezone import now
from django.forms import model_to_dict

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

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    desc = models.TextField(blank=True,null=True, verbose_name='Descripción')
    
    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

gender_choices = (
    ('male','Masculino'),
    ('female','Femenino'),
)

class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    birthday = models.DateField(default=now, verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    sexo = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


class Sale(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.names

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']




