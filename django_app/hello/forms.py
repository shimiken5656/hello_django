from django import forms
from.models import Friend, Message

class HelloForm(forms.Form):
    id = forms.IntegerField(label='ID')


class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

#P191 FriendForm書いてなかったかも
class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name','mail','gender','age','birthday']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title','content','friend']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'content': forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':2}),
            'friend': forms.Select(attrs={'class':'form-control form-control-sm'}),
        }