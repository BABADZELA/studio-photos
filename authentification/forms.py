from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    username = forms.CharField(max_length=70, label="Nom d'utilisateur")
    password = forms.CharField(max_length=70, widget=forms.PasswordInput, label="Mot de passe")

# on crée un formulaire d'inscription grace à la classe UserCreationForm
class SignupForm(UserCreationForm):
    # UserCreationForm est un model Form ce qui nous permet d'utiliser la classe Meta
    class Meta(UserCreationForm.Meta):
        model = get_user_model() # modèle utilisateur
        fields = ['username', 'email', 'first_name', 'last_name', 'role']