from django.urls import path
from . import views
from users.views import logout_view

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
