from django.urls import path 
from ERPapp.views.category.views import *
from ERPapp.views.product.views import *
from ERPapp.views.dashboard.views import *
app_name='erp'

urlpatterns = [
    path('category/list/',CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='create_category'),
    path('category/update/<int:pk>/',CategoryUpdateView.as_view(),name='update_category'),
    path('category/delete/<int:pk>/',CategoryDeleteView.as_view(),name='delete_category'),
    path('category/form/',CategoryFormView.as_view(),name='form_category'),
    path('dashboard/',DashboardView.as_view(),name='dashboard'),
    path('product/list/',ProductListView.as_view(), name='product_list')

]
