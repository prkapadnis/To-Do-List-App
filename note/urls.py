from collections import namedtuple
from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.dashboard, name='Dashboard'),
    path('create/', views.createNote_view, name='create'),
    path('update/<str:id>', views.updateNote_view, name='update'),
]
