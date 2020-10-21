from django import forms


class HelloForm(forms.Form):
    id = forms.IntegerField(label='ID')


class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
