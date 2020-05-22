from django import forms


class forma(forms.Form):
    f = forms.CharField(required=True, label='Función a Integrar',
                        widget=forms.TextInput(attrs={'placeholder': 'e.g. x**2-10*x+2'}))
    I1 = forms.FloatField(required=True, label='Punto Inicial', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '1.0'}))
    I2 = forms.FloatField(required=True, label='Punto Final', initial=10.0,
                          widget=forms.TextInput(attrs={'placeholder': '10'}))
