from django.urls import path
from users.views import register_view, auth_login_view, user_list_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', auth_login_view, name='login'),
    path('users_list/', user_list_view, name='users_list'),
]