from django.urls import path
from .views import user_login, home,user_logout

urlpatterns = [
    path('', user_login, name='login'),
    path('home/', home, name='home'),
    path('user_logout/', user_logout, name='user_logout'),
]