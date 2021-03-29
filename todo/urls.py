from categories.models import Category
from django.contrib import admin
from django.urls import path
from tasks.views import TaskView
from categories.views import CategoryView
from users.views import UserView
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin', LoginView.as_view(), name='rest_login'),
    path('signup', RegisterView.as_view(), name='rest_register'),
    path('user/<int:pk>', UserView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('task/create', TaskView.as_view({'post': 'create'})),
    path('task/<int:pk>', TaskView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('task>', TaskView.as_view({'get': 'list'})),
    path('category/<int:pk>', CategoryView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('category', CategoryView.as_view({'get': 'list'})),
    path('category/create', CategoryView.as_view({'post':'create'}))
]
