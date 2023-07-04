from django.forms import *
from .models import Category


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True


    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre de la categoria',
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Ingrese una descripción de la categoria',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
        
    """def clean(self):
        cleaned = super().clean()
        if len(cleaned['name'])<=50:
            raise forms.ValidationError('Name error')
        return cleaned"""