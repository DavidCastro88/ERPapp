from django.shortcuts import render
from ERPapp.models import Product
from django.views.generic import ListView,CreateView, UpdateView, DeleteView
from django.http import JsonResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from ERPapp.forms import CategoryForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

class ProductListView(ListView):
    model = Product
    template_name = 'product/list.html'

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Product.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    
    #Sobreescribimos el metodo get_context  para poder añadir elementos que va retornar la vista en este caso añadimos el title 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de Productos'
        context['create_url'] = reverse_lazy('erp:product_list')
        context['entity'] = 'Productos'
        context['list_url'] = reverse_lazy('erp:product_list')
        return context