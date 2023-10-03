from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='home')  # the '' is for the home page, as_view() renders the class as view

]
