from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import UserLoginView, UserProfileView, UserRegisterView, delete_photo

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', login_required(LogoutView.as_view()), name='logout'),

    path('registration/', UserRegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),

    path('delete_photo/<int:user_id>', delete_photo, name='delete_photo'),
]
