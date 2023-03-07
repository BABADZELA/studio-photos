from django.urls import path
# cette page peut être générer sans avoir à créer une vue contenant 
# tout le processus contenue dans la vue LoginPage (cela permet de gagner du temps)
# (utilisation des vues générics)
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from .views import login_page, logout_user, LoginPage, signup_page

app_name = 'authentification'

urlpatterns = [
    # path('', LoginPage.as_view(), name='login'),
    path('', LoginView.as_view(template_name='authentification/login.html',
                               redirect_authenticated_user=True
                               ), name='login'),
    # path('logout/', logout_user , name='logout'),
    path('logout/', LogoutView.as_view(
        next_page='blog:home' # si ce paramètre n'est pas indiqué par défaut djangoi cherche dans la 
        # variable settings.LOGOUT_REDIRECT_URL (https://docs.djangoproject.com/fr/3.1/topics/auth/default/#how-to-log-a-user-out)
    ) , name='logout'),

    path('password_change/', PasswordChangeView.as_view(
        template_name='authentification/password_change.html', # si ce paramètre n'est pas indiqué par défaut 
        # django cherche dans le dossier  registration/password_change_form.html 
        # (https://docs.djangoproject.com/fr/3.1/topics/auth/default/#how-to-log-a-user-out)
        success_url = 'blog:home',
    ) , name='password_change'),

    path('signup/', signup_page, name='signup'),

]