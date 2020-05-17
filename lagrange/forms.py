from django import forms

# from django.core.validators import MaxValueValidator, MinValueValidator

op1 = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10)
)


class In(forms.Form):
    numero_datos = forms.ChoiceField(choices=op1)


# class datos(forms.Form):
#    def __init__(self, n, *args, **kwargs):
#        super(datos, self).__init__(*args, **kwargs)
#        self.resul = {"titulos": ["x", "f(x)"], "datos": []}
#        for i in range(0, n):
#            self.resul["datos"].append([forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': '0.0'})),
#                                        forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': '0.0'}))])

class datos(forms.Form):
    resul = {"titulos": ["x", "f(x)"], "datos": []}

    x0 = forms.FloatField(required=True, label='Valor  x0', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))
    y0 = forms.FloatField(required=True, label='Valor  y0', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))
    x1 = forms.FloatField(required=True, label='Valor  x1', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))
    y1 = forms.FloatField(required=True, label='Valor  y1', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))
    x2 = forms.FloatField(required=True, label='Valor  x2', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))
    y2 = forms.FloatField(required=True, label='Valor  y2', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))
    x3 = forms.FloatField(required=True, label='Valor  x3', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))
    y3 = forms.FloatField(required=True, label='Valor  y3', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))
    x4 = forms.FloatField(required=True, label='Valor  x4', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))
    y4 = forms.FloatField(required=True, label='Valor  y4', initial=1.0,
                          widget=forms.TextInput(attrs={'placeholder': '0.0'}))
