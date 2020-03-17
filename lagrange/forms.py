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

    x = forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': '0.0'}))
    fx = forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': '0.0'}))
