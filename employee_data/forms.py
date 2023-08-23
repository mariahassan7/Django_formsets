from django import forms
from employee_data.models import Employee
from django.forms.models import formset_factory
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ( 
            'name', 'designation', 'bio', 'skills', 'upload_image'
        )
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'designation' : forms.TextInput(attrs={'class': 'form-control'}),
            'bio' : forms.Textarea(attrs={'class': 'form-control','rows' : 3}),
            'skills' : forms.Textarea(attrs={'class': 'form-control', 'rows' : 3}),
            'upload_image' : forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
        }  


EmployeeFormset = formset_factory(EmployeeForm, extra=1)