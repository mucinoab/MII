from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class In(forms.Form):  # Input de cuantas funciones
    n = forms.IntegerField(required=True, label='',
                           widget=forms.TextInput(attrs={'placeholder': 'Solo números entre 1 y 3'}),
                           validators=[MinValueValidator(1), MaxValueValidator(3)])


class E1(forms.Form):  # Input para soo una función
    fx = forms.CharField(required=True, label='Función',
                         widget=forms.TextInput(attrs={'placeholder': 'e.g. x**3+4*x**2-10'}))
    x0 = forms.FloatField(required=True, label='Valor Inicial', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))


class E2(forms.Form):  # Input para 2 funciones
    fx = forms.CharField(required=True, label='Función 1',
                         widget=forms.TextInput(attrs={'placeholder': 'e.g. x**2-10*x+y**2+8'}))
    x0 = forms.FloatField(required=True, label='Valor Inicial x', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))

    fy = forms.CharField(required=True, label='Función 2',
                         widget=forms.TextInput(attrs={'placeholder': 'e.g. x**2-10*x+y**2+8'}))

    y0 = forms.FloatField(required=True, label='Valor Inicial y', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))


class E3(forms.Form):  # Input para 2 funciones
    fx = forms.CharField(required=True, label='Función 1',
                         widget=forms.TextInput(attrs={'placeholder': 'e.g. x**2-10*x+y**2+8'}))
    x0 = forms.FloatField(required=True, label='Valor Inicial x', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))

    fy = forms.CharField(required=True, label='Función 2',
                         widget=forms.TextInput(attrs={'placeholder': 'e.g. x**2-10*x+y**2+8'}))

    y0 = forms.FloatField(required=True, label='Valor Inicial y', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))

    fz = forms.CharField(required=True, label='Función 3',
                         widget=forms.TextInput(attrs={'placeholder': 'e.g. z**2-x**2-10*x+y**2+8+z'}))

    z0 = forms.FloatField(required=True, label='Valor Inicial z', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))
