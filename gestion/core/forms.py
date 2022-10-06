from django.forms import ModelForm,widgets,TextInput,Textarea
from .models import *

class CategoryForm(ModelForm):
    #def __init__(self,*args,**kwargs):
    #    super().__init__(*args,**kwargs)
    #    for form in self.visible_fields():
    #        form.fields.widgets.attrs['class']='form-control'
    
    class Meta:
        model=Category
        fields='__all__'

    def save(self, commit=True):
        data={}
        form=super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error']=form.errors
        except Exception as e:
            data['error']=str(e)
        return data

class ProductForm(ModelForm):
    #def __init__(self,*args,**kwargs):
    #    super().__init__(*args,**kwargs)
    #    for form in self.visible_fields():
    #        form.fields.widgets.attrs['class']='form-control'
    
    class Meta:
        model=Producto
        fields='__all__'

