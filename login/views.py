from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect,HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.views.generic import FormView, RedirectView
from ERP.settings import LOGIN_REDIRECT_URL

class LoginFormView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] ='Iniciar Sesión' 
        return context
    
class LoginFormView2(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy(LOGIN_REDIRECT_URL)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self,form):
        login(self.request,form.get_user())
        return HttpResponseRedirect(self.success_url)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] ='Iniciar Sesión' 
        return context
    
class LogoutRedirectView(RedirectView):
    pattern_name ='index'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
    
