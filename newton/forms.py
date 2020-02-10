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
    f       = forms.CharField(required=True, label='Función a Resolver', initial='x**2+3*x-15', widget=forms.TextInput(attrs={'placeholder':'e.g. x**2-1'}))
    ini     = forms.FloatField(required=False, label='Valor Inicial', initial=0.0, widget=forms.TextInput(attrs={'placeholder':'0.0'}))
