from django import forms
from First.models import Employee

class EmpForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=["ename","eemail","econtact"]