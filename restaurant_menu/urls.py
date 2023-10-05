from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),  # the '' is for the home page, as_view() renders the class as view
    path('item/<int:pk>/', views.MenuItemDetail.as_view(), name="menu_item")  # another view for handling individual
    # subdirectory
]
