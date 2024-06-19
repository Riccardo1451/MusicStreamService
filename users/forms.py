from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#volgiamo inserire un campo email nel form
#per farlo estendiamo la classe base UserCreationForm e aggiungiamo un campo

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #required

    class Meta:
        model = User #modello con cui interagisce
        fields = ['username', 'email', 'password1', 'password2'] #campi che appaiono nel form