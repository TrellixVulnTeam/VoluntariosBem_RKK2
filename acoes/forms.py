from django import forms

class CadastroVoluntario(forms.Form):
    user = forms.CharField(label='Usuário')
    email = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    avatar = forms.ImageField()