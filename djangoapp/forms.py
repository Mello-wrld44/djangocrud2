from django import forms
from djangoapp.models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['firstname','lastname','email']