from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class In(forms.Form):  # Input de cuantas funciones
    n = forms.IntegerField(required=True, label='',
                           widget=forms.TextInput(attrs={'placeholder': 'Solo números entre 2 y 4'}),
                           validators=[MinValueValidator(2), MaxValueValidator(4)])


class E2(forms.Form):  # Input para 2 funciones
    f1 = forms.CharField(required=True, label='Función 1',
                         widget=forms.TextInput(attrs={'placeholder': 'e.g. x**2-10*x+y**2+8'}))
    x0 = forms.FloatField(required=True, label='Valor Inicial x', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))

    f2 = forms.CharField(required=True, label='Función 2',
                         widget=forms.TextInput(attrs={'placeholder': 'e.g. x**2-10*x+y**2+8'}))

    y0 = forms.FloatField(required=True, label='Valor Inicial y', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))


class E3(forms.Form):  # Input para 2 funciones
    f1 = forms.CharField(required=True, label='Función 1',
                         widget=forms.TextInput(attrs={'placeholder': 'e.g. x**2-10*x+y**2+8*z'}))
    x0 = forms.FloatField(required=True, label='Valor Inicial x', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))

    f2 = forms.CharField(required=True, label='Función 2',
                         widget=forms.TextInput(attrs={'placeholder': 'e.g. z*x**2-10*x+y**2+8'}))

    y0 = forms.FloatField(required=True, label='Valor Inicial y', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))

    f3 = forms.CharField(required=True, label='Función 3',
                         widget=forms.TextInput(attrs={'placeholder': 'e.g. z**2-x**2-10*x+y**2+8+z'}))

    z0 = forms.FloatField(required=True, label='Valor Inicial z', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))


class E4(forms.Form):  # Input para 2 funciones
    f1 = forms.CharField(required=True, label='Función 1',
                         widget=forms.TextInput(attrs={'placeholder': 'e.g.z*w+x**2-10*x+y**2+8'}))
    x0 = forms.FloatField(required=True, label='Valor Inicial x', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))

    f2 = forms.CharField(required=True, label='Función 2',
                         widget=forms.TextInput(attrs={'placeholder': 'e.g. z*w+x**2-10*x+y**2+8'}))

    y0 = forms.FloatField(required=True, label='Valor Inicial y', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))

    f3 = forms.CharField(required=True, label='Función 3',
                         widget=forms.TextInput(attrs={'placeholder': 'e.g. z*w+**2-x**2-10*x+y**2+8+z'}))

    z0 = forms.FloatField(required=True, label='Valor Inicial z', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))

    f4 = forms.CharField(required=True, label='Función 4',
                         widget=forms.TextInput(attrs={'placeholder': 'e.g. w*x*z**2-10*x+y**2+8'}))

    w0 = forms.FloatField(required=True, label='Valor Inicial w', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))
