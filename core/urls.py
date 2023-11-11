from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import LoginForm
from django.contrib.auth.views import LogoutView

from . import views
# from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('privacy_and_policy/', views.privacy_and_policy, name='privacy'),
    path('terms_of_use/', views.terms_of_use, name='terms_of_use'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('get_cities/', views.get_cities, name='get_cities'),
    path('profile/<str:user>/', views.profile, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/<str:user>/', views.dashboard, name='dashboard'),
    path('profile/edit/<str:user>/', views.profile_edit, name='profile_edit'),
]
