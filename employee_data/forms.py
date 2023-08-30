from django import forms
from employee_data.models import Employee
from django.forms.models import modelformset_factory
class EmployeeForm(forms.ModelForm):
    class Meta:
        fields = ( 
            'name', 'designation', 'bio', 'skills'
            # , 'upload_image'
        )
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'designation' : forms.TextInput(attrs={'class': 'form-control'}),
            'bio' : forms.Textarea(attrs={'class': 'form-control','rows' : 3}),
            'skills' : forms.Textarea(attrs={'class': 'form-control', 'rows' : 3}),
            # 'upload_image' : forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
        }  

EmployeeFormset = modelformset_factory(Employee, form=EmployeeForm, extra=1)