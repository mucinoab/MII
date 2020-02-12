from django import forms
from .models import Input

# class product (forms.ModelForm):
#     class Meta:
#         model = Input
#         valores = [
#             'func',
#             'inicial'
#         ]

class In(forms.Form):
    f       = forms.CharField(required=True, label='f(x)', widget=forms.TextInput(attrs={'placeholder':'e.g. x**2-2*x-sin(x)*exp(x)'}))
    ini     = forms.FloatField(required=False, label='Valor inicial', initial=1.0, widget=forms.TextInput(attrs={'placeholder':'0.0'}))