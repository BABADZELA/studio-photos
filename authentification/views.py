from django.contrib.auth import login, authenticate, logout # import des fonctions login et authenticate
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import LoginForm, SignupForm

class LoginPage(View):
    # le foemulaire de la page de connexion
    form_class = LoginForm
    template_name = 'authentification/login.html'

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        message = ''
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
                return redirect('blog:home')
            else:
                message = 'Identifiants invalides.'
        return render(request, self.template_name, context={'form': form, 'message': message})

def login_page(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
                return redirect('blog:home')
            else:
                message = 'Identifiants invalides.'
    return render(request, 'authentification/login.html', context={'form': form, 'message': message})

def logout_user(request):
    logout(request)
    return redirect('authentification:login')

def signup_page(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:home')
    return render(request, 'authentification/signup.html', context={'form': form,})
