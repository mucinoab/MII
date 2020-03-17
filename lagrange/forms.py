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

class datos(forms.Form):
    def __init__(self, n, *args, **kwargs):
        super(datos, self).__init__(*args, **kwargs)
        self.resul = {"titulos": ["x", "f(x)"], "datos": []}
        for i in range(0, n):
            self.resul["datos"].append([forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': '0.0'})),
                                        forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': '0.0'}))])














