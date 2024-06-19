from .models import students
from django import forms
class inputform(forms.ModelForm):
    class Meta:
        model=students
        fields=['First_Name','USN','College','Course','Contact_Number']