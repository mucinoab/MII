from django import forms


class forma(forms.Form):
    f = forms.CharField(required=True, label='Función a Integrar',
                        widget=forms.TextInput(attrs={'placeholder': 'e.g. 1/x'}))
    a = forms.FloatField(required=True, label='Punto Inicial', initial=1.0,
                         widget=forms.TextInput(attrs={'placeholder': '1.0'}))
    b = forms.FloatField(required=True, label='Punto Final', initial=15.0,
                         widget=forms.TextInput(attrs={'placeholder': '5.0'}))
    n = forms.FloatField(required=True, label='Número de subintervalos', initial=10.0,
                         widget=forms.TextInput(attrs={'placeholder': '4'}))
