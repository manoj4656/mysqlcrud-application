from django import forms
from mysqlcrudapp.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'mail':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
        }