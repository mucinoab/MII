from django import forms

class datos(forms.Form):
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

